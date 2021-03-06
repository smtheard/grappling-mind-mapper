from config import app
from bottle import static_file


@app.get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(
        filepath, root='./static')  # relative to server.py, not this file.
