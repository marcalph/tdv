""" implement a basic http server that handles
    GET/POST requests on all paths/subpaths
"""
# stdlib
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging


class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info(f"GET route {self.path}\nHeaders: {self.headers}")
        self._set_response()
        self.wfile.write(f"GET {self.path}\n".encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        posted_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info(f"POST route {self.path}\nHeaders: {self.headers}\nBody: {posted_data}")
        self._set_response()
        self.wfile.write(f"POST {self.path}\n".encode('utf-8'))


logging.basicConfig(level=logging.INFO)
server_address = ('', 8000)
httpd = HTTPServer(server_address, RequestHandler)
httpd.serve_forever()