from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("Received GET request")
        # Send response status code
        self.send_response(200)
        # End headers
        self.end_headers()
        # The server will not send any content back (as per your request)
        return

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving HTTP on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping HTTP server...')

if __name__ == '__main__':
    run()