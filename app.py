import http.server
import socketserver
from http import HTTPStatus
import camelcase

c = camelcase.CamelCase()

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(c.hump('hello world').encode())

httpd = socketserver.TCPServer(('', 8080), Handler)
httpd.serve_forever()
