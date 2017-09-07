# python3 -m http.server 8000
# python3 -m http.server 8010 --bind 127.0.0.1
# python3 -m http.server --cgi 8000


# Pure Python Server
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler # 핸들러 설정

# 소켓 열기
with socketserver.TCPServer(("", PORT), Handler) as httpd: # wita as 문 : 해당 블럭이 끝나면 소멸.
    print("server at port", PORT)
    httpd.serve_forever()                    # 서버 시작