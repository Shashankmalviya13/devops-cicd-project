
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class DevOpsHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            data = {
                "status": "healthy",
                "application": "Python DevOps Project"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()

            html = """
            <h1>My First DevOps Project</h1>
            <p>Python application is running!</p>
            <p>GitHub Actions + Docker + CI/CD</p>
            <a href="/health">Check Health</a>
            """
            self.wfile.write(html.encode())


if __name__ == "__main__":
    
    server = HTTPServer(("0.0.0.0", 8000), DevOpsHandler)
    
    print("Server running at http://localhost:8000")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()

