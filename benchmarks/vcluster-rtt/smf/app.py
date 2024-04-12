from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Get the path from the request
        path = self.path
        print(f"Request path: {path}")

        # Depending on the path, the behavior changes
        if path == '/create-sm-context':
            self.handle_create_sm_context()
        elif path == '/update-sm-context':
            self.handle_update_sm_context()
        else:
            # Default handling for other paths
            self.handle_default()

    def handle_create_sm_context(self):

        requests.get('http://upf.default.svc.cluster.local:80/pfcp-sess-est-request')

        self.send_response(200)
        self.end_headers()

    def handle_update_sm_context(self):

        requests.get('http://upf.default.svc.cluster.local:80/pfcp-sess-modify-request')

        self.send_response(200)
        self.end_headers()

    def handle_default(self):
        # General handling for unspecified paths
        print("Unrecognized path, sending 404 Not Found")
        self.send_response(404)
        self.end_headers()

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