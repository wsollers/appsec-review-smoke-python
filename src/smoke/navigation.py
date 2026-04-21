"""Redirect helpers for the smoke service. Deliberately vulnerable smoke target; see README.md."""
from flask import redirect


def return_to(target):
    """Sends the client to the page named by the request's return parameter."""
    return redirect(target)
