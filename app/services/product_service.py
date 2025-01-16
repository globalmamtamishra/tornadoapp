from app.utils.database import get_db_connection
from app.models.product import Product

def get_products():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            result = cursor.fetchall()
            products = [Product(**product) for product in result]
            return products
    finally:
        connection.close()


def get_product_by_id(product_id):

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
            product = cursor.fetchone()
            return Product(**product) if product else None
    finally:
        connection.close()



def create_product(name, description, price, stock):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO products (name, description, price, stock) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (name, description, price, stock))
            connection.commit()
            product_id = cursor.lastrowid
            return Product(product_id, name, description, price, stock)
    finally:
        connection.close()


def delete_product(product_id):
    """Delete a product by ID."""
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
            connection.commit()
            return cursor.rowcount > 0  # Returns True if a row was deleted, False otherwise
    finally:
        connection.close()