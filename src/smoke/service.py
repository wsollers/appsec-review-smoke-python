"""Request dispatcher for the smoke service. Deliberately vulnerable smoke target; see README.md."""
import logging

from flask import Flask, request

from smoke import maintenance, navigation, tools

app = Flask(__name__)
LOG = logging.getLogger("smoke")
VERSION = "0.1.0"
MAX_LIMIT = 50
_requests = 0


@app.route("/api/<path:path>")
def api(path):
    return handle_request(path, request.args)


def handle_request(path, args):
    """Dispatches one API request by path and returns the reply body."""
    global _requests
    reply = None
    status = 400
    if path.endswith("/"):
        path = path[:-1]
    if path == "status":
        reply = "ok " + VERSION
        status = 200
    elif path == "echo":
        reply = args.get("text", "")
        status = 200
    elif path == "lookup" and "name" in args:
        name = args["name"]
        LOG.info("lookup for " + name)
        reply = name.upper() if args.get("upper") else name
        status = 200
    elif path == "config":
        key = args.get("key", "")
        if key in ("debug", "verbose"):
            reply = key + "=on"
            status = 200
        else:
            status = 404
    elif path == "return":
        return navigation.return_to(args.get("next", "/"))
    elif path == "formula":
        value = tools.evaluate_known(args.get("expr", ""))
        reply = str(value)
        status = 200 if value is not None else 404
    elif path == "scale":
        reply = str(tools.scale(args.get("value", "0")))
        status = 200
    elif path == "archive" and "name" in args:
        reply = maintenance.archive(args["name"])
        status = 200
    elif path == "report" and "name" in args:
        reply = maintenance.read_report(args["name"])
        status = 200
    elif path == "page":
        raw = args.get("limit", "10")
        limit = int(raw) if raw.isdigit() else 10
        if limit < 1 or limit > MAX_LIMIT:
            limit = MAX_LIMIT
        reply = "\n".join(str(i) for i in range(limit))
        status = 200
    elif path == "headers":
        wanted = [h for h in ("User-Agent", "Accept") if h in args and args[h]]
        reply = ", ".join(wanted) or "none"
        status = 200
    if status >= 200 and status < 300:
        _requests += 1
    if reply is None:
        reply = "error"
    return str(status) + " " + reply + " X-Count: " + str(_requests)


def main():
    if not tools.self_test():
        raise SystemExit("self test failed")
    app.run()


if __name__ == "__main__":
    main()
