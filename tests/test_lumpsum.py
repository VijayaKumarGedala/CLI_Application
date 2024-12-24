"""This is test module to test investments
"""

import pytest
from calculator.investments.lumpsum import LumpsumInvestment
from calculator.investments.exceptions import (
    InvalidInvestmentAmount,
    InvalidInvestmentReturns,
    InvalidInvestmentTime,
)


def test_lumpsum_investment_positive():
    """This module tests the Lumpsum investment
    with positive values
    """
    investment = LumpsumInvestment(1000, 10, 1)
    assert investment.amount == 1000
    assert investment.rate == 10
    assert investment.calculate() == 1100


def test_lumpsum_investment_exceptions():
    """
    This test focuses on exception scenarios
    """

    with pytest.raises(InvalidInvestmentAmount):
        investment = LumpsumInvestment(amount=0, rate=10, time=1)
        investment.calculate()

    with pytest.raises(InvalidInvestmentReturns):
        investment = LumpsumInvestment(amount=1000, rate=0, time=1)
        investment.calculate()

    with pytest.raises(InvalidInvestmentTime):
        investment = LumpsumInvestment(amount=1000, rate=10, time=0)
        investment.calculate()
