import http.server

PORT = 8080

class Handler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ['/cgi'] # CGI

with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print("server is running", PORT)
    httpd.serve_forever()
