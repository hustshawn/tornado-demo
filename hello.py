import tornado.ioloop
import tornado.web

from tornado.options import define, options
define("port", default=8888, help="Server running on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = make_app()
    application.listen(options.port)
    print("Server is running on http://localhost:" + str(options.port))
    tornado.ioloop.IOLoop.current().start()