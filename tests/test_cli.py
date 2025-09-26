import math
import sys
import pytest
from calculator.__main__ import main, cli

def run_cli(args, capsys):
    exit_code = main(["calculator"] + args)
    captured = capsys.readouterr()
    return exit_code, captured.out.strip(), captured.err

@pytest.mark.parametrize(
    "args,expected",
    [
        (["add", "2", "3"], "5"),
        (["sub", "10", "4"], "6"),
        (["mul", "6", "7"], "42"),
        (["div", "20", "5"], "4.0"),
    ],
)
def test_cli_ok(args, expected, capsys):
    code, out, _ = run_cli(args, capsys)
    assert code == 0
    assert out == expected

def test_cli_divide_by_zero(capsys):
    code, out, _ = run_cli(["div", "1", "0"], capsys)
    assert code == 1
    assert out.startswith("Error: Cannot divide by zero.")

def test_cli_bad_args_count(capsys):
    code, out, _ = run_cli(["add", "2"], capsys)
    assert code == 2
    assert "Usage:" in out

def test_cli_non_numeric(capsys):
    code, out, _ = run_cli(["add", "a", "2"], capsys)
    assert code == 2
    assert "must be numbers" in out

def test_cli_unknown_op(capsys):
    code, out, _ = run_cli(["pow", "2", "3"], capsys)
    assert code == 2
    assert "Unknown operation" in out

def test_entrypoint_cli_calls_main(monkeypatch):
    called = {}
    def fake_main(argv):
        called["argv"] = argv
        return 0

    import calculator.__main__ as m
    monkeypatch.setattr(m, "main", fake_main)
    argv = ["calculator", "add", "1", "2"]
    monkeypatch.setattr(sys, "argv", argv)
    assert cli() == 0
    assert called["argv"] == argv
