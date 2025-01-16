import tornado.ioloop
import tornado.web

from app.handlers.product_handler import ProductHandler

def make_app():
    return tornado.web.Application([
        (r"/products", ProductHandler),
        (r"/products/(\d+)", ProductHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8885)
    print("Server is running at http://localhost:8885")
    tornado.ioloop.IOLoop.current().start()
