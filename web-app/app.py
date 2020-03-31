import os

import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

WEB_APP_PORT=int(8888)

define("port", default=WEB_APP_PORT, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly interviewer.')

    def write_error(self, status_code, **kwargs):
        self.write("There was a %d error." % status_code)

class RequestHandler(tornado.web.RequestHandler):
    def get(self):
        message = "Please Hire Eric Toner"
        self.write(message)

    def write_error(self, status_code, **kwargs):
        self.write("There was a %d error." % status_code)

class ResumeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def write_error(self, status_code, **kwargs):
        self.write("There was a %d error." % status_code)

def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
        (r"/request", RequestHandler),
        (r"/resume", ResumeHandler),
    ])

#

if __name__ == "__main__":
    app = make_app()
    app.listen(WEB_APP_PORT)
    tornado.ioloop.IOLoop.current().start()
