import http.server, functools, os
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        super().end_headers()
    def log_message(self, *a): pass
d = os.path.expanduser("~/pacific-galleon")
http.server.ThreadingHTTPServer(("127.0.0.1", 8914),
    functools.partial(H, directory=d)).serve_forever()
