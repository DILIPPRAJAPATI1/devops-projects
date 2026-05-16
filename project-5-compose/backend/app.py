from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Backend")

server = HTTPServer(('0.0.0.0', 5000), SimpleHandler)
server.serve_forever()
