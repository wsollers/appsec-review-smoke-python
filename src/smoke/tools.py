"""Formula helpers for the smoke service. Deliberately vulnerable smoke target; see README.md."""


def self_test():
    """Checks that the interpreter evaluates a constant formula as expected."""
    return eval("1 + 1") == 2
