from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import requests


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Get the path from the request
        path = self.path
        print(f"Request path: {path}")

        # Depending on the path, the behavior changes
        if path == '/slice-selection-get':
            self.handle_slice_selection_get()
        elif path == '/am-subscription-get':
            self.handle_am_subscription_get()
        elif path == '/sm-subscription-get':
            self.handle_sm_subscription_get()
        elif path == '/sdm-subscription':
            self.handle_sdm_subscription()
        else:
            # Default handling for other paths
            self.handle_default()

    def handle_slice_selection_get(self):
        self.send_response(200)
        self.end_headers()

    def handle_am_subscription_get(self):
        self.send_response(200)
        self.end_headers()

    def handle_sm_subscription_get(self):
        self.send_response(200)
        self.end_headers()
    
    def handle_sdm_subscription(self):
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