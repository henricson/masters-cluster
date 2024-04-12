from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import requests


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Get the path from the request
        path = self.path
        print(f"Request path: {path}")

        # Depending on the path, the behavior changes
        if path == '/ue-authentication-info':
            self.handle_ue_authentication_info()
        elif path == '/5g-aka-confirmation':
            self.handle_aka_confirmation()
        else:
            # Default handling for other paths
            self.handle_default()

    def handle_ue_authentication_info(self):
        response = requests.get('http://udm.default.svc.cluster.local:80')
        print(f"Response from UDM for /path1: {response.status_code}")

        # Send a successful response
        self.send_response(200)
        self.end_headers()

    def handle_aka_confirmation(self):
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