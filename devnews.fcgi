#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from devnews.web import APP

if __name__ == '__main__':
    WSGIServer(APP).run()
