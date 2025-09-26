"""CLI entry for the calculator package."""
import sys
from .calc import add, subtract, multiply, divide

def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print("Usage: python -m calculator <add|sub|mul|div> <a> <b>")
        return 2

    op, a_str, b_str = argv[1], argv[2], argv[3]
    try:
        a = float(a_str) if "." in a_str else int(a_str)
        b = float(b_str) if "." in b_str else int(b_str)
    except ValueError:
        print("Arguments <a> and <b> must be numbers.")
        return 2

    try:
        if op in ("add", "+"):
            result = add(a, b)
        elif op in ("sub", "-"):
            result = subtract(a, b)
        elif op in ("mul", "*", "x"):
            result = multiply(a, b)
        elif op in ("div", "/"):
            result = divide(a, b)
        else:
            print("Unknown operation. Use add|sub|mul|div")
            return 2
    except Exception as exc:  # pylint: disable=broad-except
        print(f"Error: {exc}")
        return 1

    print(result)
    return 0

def cli() -> int:
    """Console script entrypoint (used by packaging)."""
    return main(sys.argv)

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
