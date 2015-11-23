__author__ = 'lqe'
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def _writeheaders(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def do_HEAD(self):
        self._writeheaders()

    def do_GET(self):
        self._writeheaders()
        self.wfile.write('''<HTML>
        <HEAD><TITLE>SAMPLE PAGE</TITLE></HEAD>
        <BODY>This is a sample HTML page. Every page this server provides will look like this.</BODY></HTML>''')

serveraddr = ('',8765)
srvr = HTTPServer(serveraddr, RequestHandler)
srvr.serve_forever()


