from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from address_to_coords import address_to_coords

class AddressRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        # send headers
        self.send_header('Content-type','text/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        # send response status code
        self.send_response(200)

    def do_POST(self):
        self._set_headers()

        content_len = int(self.headers['content-length'])
        data_string = self.rfile.read(content_len).decode('utf-8')
        data_obj    = json.loads(data_string)

        if "address" in data_obj:
            address = data_obj["address"]
            coords  = address_to_coords(address)
            self.send_response(200)
            # send coordinates in response
            self.wfile.write(bytes(str(coords), "utf-8"))
            return

        else:
            self.send_response(400)
            return

        self.send_response(500)
        return

def serve(handler=AddressRequestHandler, port=6305):
    server_address = ("", port)
    httpd = HTTPServer(server_address, handler)
    print("starting server on port", port)
    httpd.serve_forever()