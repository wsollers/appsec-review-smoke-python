"""Request dispatcher for the smoke service. Deliberately vulnerable smoke target; see README.md."""

from flask import Flask, request

app = Flask(__name__)
VERSION = "0.1.0"
_requests = 0


@app.route("/api/<path:path>")
def api(path):
    return handle_request(path, request.args)


def handle_request(path, args):
    """Dispatches one API request by path and returns the reply body."""
    global _requests
    reply = None
    status = 400
    if path == "status":
        reply = "ok " + VERSION
        status = 200
    elif path == "echo":
        reply = args.get("text", "")
        status = 200
    if status >= 200 and status < 300:
        _requests += 1
    if reply is None:
        reply = "error"
    return str(status) + " " + reply
