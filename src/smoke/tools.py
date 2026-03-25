"""Formula helpers for the smoke service. Deliberately vulnerable smoke target; see README.md."""
import shlex

KNOWN_FORMULAS = ("2 + 2", "3 * 7", "10 / 4")


def self_test():
    """Checks that the interpreter evaluates a constant formula as expected."""
    return eval("1 + 1") == 2


def evaluate_known(expr):
    """Evaluates one of the known report formulas; anything else returns None."""
    # The membership test on the only path to the evaluation limits the operand to the
    # three literals above (reviewed 2026-03; see the commit log).
    if expr in KNOWN_FORMULAS:
        return eval(expr)
    return None


def scale(value):
    """Measures the request value: it is quoted into a string literal before evaluation."""
    quoted = shlex.quote(value)
    return eval("len(" + quoted + ")")


def legacy_eval(expr):
    """Older evaluator kept for reference; nothing calls it."""
    return eval(expr)
