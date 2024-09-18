from src.endpoints import get_root, get_brightness, set_brightness
from lib.http.server import Server

app = Server()

app.add_route("/", "GET", get_root)
app.add_route("/brightness", "GET", get_brightness)
app.add_route("/brightness", "POST", set_brightness)

if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 8080
    app.listen(ip, port, lambda: print(f"Listening at {ip}:{port}"))