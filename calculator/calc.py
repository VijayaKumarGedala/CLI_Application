"""caclulator.py

This module is the main application 
This contains functionality to validate command line arguments

usage:
  calc.py --type sip --amount 5000 --time 10 --rate 12
  11,61,695

  calc.py --type fd --amount 100 --time 1 --rate 7
  107
"""

import argparse
# fix for running with python calc.py
import sys
import os

# Add the parent directory of my_cli_app to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator.investments.lumpsum import LumpsumInvestment
from calculator.investments.monthly import MonthlyInvestment


def create_parser() -> argparse.ArgumentParser:
    """
    This function creates a parser

    Returns:
        argument parser (argparse.ArgumentParser)
    """
    parser = argparse.ArgumentParser(
        prog="calc", description="This investement calculator"
    )
    parser.add_argument(
        "--type", type=str, required=True, choices=["fd", "sip"], help="investment type"
    )
    parser.add_argument("--amount", type=float, required=True, help="Investment amount")
    parser.add_argument(
        "--time",
        type=int,
        required=False,
        default=10,
        help="Investment period in years",
    )
    parser.add_argument("--rate", type=float, required=True, help="Rate of Returns")
    return parser


def calcuate_returns(args) -> None:
    """This method will make necessary calls to
    calculate returns
    """
    if args.type == "fd":
        # create lumpsum caclutor and show returns
        investement_calc = LumpsumInvestment(
            amount=args.amount, time=args.time, rate=args.rate
        )
        total_value = investement_calc.calculate()
        print(f"value post {args.type} investment is {total_value}")
    elif args.type == "sip":
        # create monthly calculator and show returns
        investement_calc = MonthlyInvestment(
            amount=args.amount, time=args.time, rate=args.rate
        )
        total_value = investement_calc.calculate()
        print(f"value post {args.type} investment is {total_value}")


def main():
    """This function will create parser and get arguments"""
    parser = create_parser()
    args = parser.parse_args()
    calcuate_returns(args)


if __name__ == "__main__":
    main()
