import SimpleHTTPServer
import SocketServer

PORT = 8000


class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    "?P[-"

    def __init__(self, req, client_addr, server):
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, req, client_addr, server)

    def do_GET(self):
        # print "self.path = " + self.path;

        if 'query' in self.path:
            self.path = '/data.json'

        # cut off a query string
        if '?' in self.path:
            self.path = self.path.split('?')[0]
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    httpd = MyTCPServer(('localhost', PORT), CustomHandler)
    httpd.allow_reuse_address = True
    print "Serving at port", PORT
    httpd.serve_forever()
