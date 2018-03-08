from tornado.web import Application
from tornado.ioloop import IOLoop


class ChatServer(object):
    def __init__(self):
        self.app = None

def make_server():
    server = ChatServer()
    server.app = Application()
    return server

def start_server(*args, **kwargs):
    server = make_server(*args, **kwargs)
    loop = IOLoop.current()
    loop.start()


if __name__ == '__main__':
    start_server()