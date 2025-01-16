import tornado.web
from app.services.product_service import get_products, get_product_by_id, create_product, delete_product

from app.handlers.base_handler import BaseHandler

class ProductHandler(BaseHandler):

    async def get(self, product_id=None):

        if product_id:
            product = get_product_by_id(product_id)
            if product:
                self.write({"product": product.__dict__})
            else:
                self.set_status(404)
                self.write({"error": "Product not found"})
        else:
            products = get_products()
            self.write({"products": [product.__dict__ for product in products]})

    async def post(self):

        data = tornado.escape.json_decode(self.request.body)
        product = create_product(data['name'], data['description'], data['price'], data['stock'])
        self.write({"product": product.__dict__})

    async def delete(self, product_id):

        success = delete_product(product_id)
        if success:
            self.write({"message": "Product deleted successfully"})
        else:
            self.set_status(404)
            self.write({"error": "Product not found"})
