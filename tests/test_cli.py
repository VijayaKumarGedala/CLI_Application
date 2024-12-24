"""This module contains tests to test the calculator cli
"""

import pytest
from unittest.mock import patch
from calculator.calc import main


def test_valid_args(capsys):
    """Test valid arguments"""
    with patch(
        "sys.argv",
        [
            "calculator/calc.py",
            "--amount",
            "1000",
            "--type",
            "fd",
            "--rate",
            "10",
            "--time",
            "1",
        ],
    ):
        main()
    captured = capsys.readouterr()
    assert "value post fd investment is 1100.0" in captured.out

    with patch(
        "sys.argv",
        [
            "calculator/calc.py",
            "--amount",
            "1000",
            "--type",
            "sip",
            "--rate",
            "10",
            "--time",
            "1",
        ],
    ):
        main()
    captured = capsys.readouterr()
    assert "value post sip investment is" in captured.out


def test_invalid_args():
    """Test Invalid arguments"""
    with patch(
        "sys.argv",
        ["calculator/calc.py", "--type", "fd", "--rate", "10", "--time", "1"],
    ):
        with pytest.raises(SystemExit):
            main()
