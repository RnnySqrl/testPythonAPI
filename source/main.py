import tornado.ioloop
import tornado.web
from routes.routes import Search_by_id
from model.model import model


def run_server():
    m = model()
    data = m.get_data()
    print("Data loaded")
    return tornado.web.Application([
        (r"/id", Search_by_id, dict(data=data)),
    ])

if __name__ == "__main__":
    app = run_server()
    app.listen(8080)
    print("Running server.... press ctrl+c to stop")
    tornado.ioloop.IOLoop.current().start()
