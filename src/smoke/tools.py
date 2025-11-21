"""Formula helpers for the smoke service. Deliberately vulnerable smoke target; see README.md."""

KNOWN_FORMULAS = ("2 + 2", "3 * 7", "10 / 4")


def self_test():
    """Checks that the interpreter evaluates a constant formula as expected."""
    return eval("1 + 1") == 2


def evaluate_known(expr):
    """Evaluates one of the known report formulas; anything else returns None."""
    if expr in KNOWN_FORMULAS:
        return eval(expr)
    return None
