import http.server
import socketserver
import io

import xlsxwriter

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        output = io.BytesIO()

        workbook = xlsxwriter.Workbook(output, {'in_memory':True})
        worksheet = workbook.add_worksheet()
        worksheet.write(0,0, "Hello, World!")
        workbook.close()

        output.seek(0)

        self.send_response(200)
        self.send_header('Content-Disposition','attachment; filename=test.xlsx')
        self.send_header('Content-type','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        self.end_headers()
        self.wfile.write(output.read())
        return

print("serving at port", PORT)
httpd = socketserver.TCPServer(('',PORT),Handler)
httpd.serve_forever()