"""
exceptions.py


This module contains necessary investment Exceptions
"""


class InvalidInvestmentType(Exception):
    """This represents Invalid Investment Type
    value should be Monthly or Yearly
    """


class InvalidInvestmentAmount(Exception):
    """This represents Zero or negative investments"""


class InvalidInvestmentReturns(Exception):
    """This represents Zero or negative Returns Rate"""


class InvalidInvestmentTime(Exception):
    """This represents Zero or negative InvestmentTime"""
