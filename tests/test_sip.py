"""This is test module to test investments
"""

import pytest
from calculator.investments.monthly import MonthlyInvestment
from calculator.investments.exceptions import (
    InvalidInvestmentAmount,
    InvalidInvestmentReturns,
    InvalidInvestmentTime,
    InvalidInvestmentType
)


def test_sip_investment_positive():
    """This module tests the Lumpsum investment
    with positive values
    """
    investment = MonthlyInvestment(1000, 10, 1)
    assert investment.amount == 1000
    assert investment.rate == 10
    assert investment.calculate() == pytest.approx(12670.28)


def test_monthly_investment_exceptions():
    """
    This test focuses on exception scenarios
    """

    with pytest.raises(InvalidInvestmentAmount):
        investment = MonthlyInvestment(amount=0, rate=10, time=1)
        investment.calculate()

    with pytest.raises(InvalidInvestmentReturns):
        investment = MonthlyInvestment(amount=1000, rate=0, time=1)
        investment.calculate()

    with pytest.raises(InvalidInvestmentTime):
        investment = MonthlyInvestment(amount=1000, rate=10, time=0)
        investment.calculate()

    with pytest.raises(InvalidInvestmentType):
        investment = MonthlyInvestment(amount=1000, rate=10, time=10)
        investment.investment_type = "Test"
        investment.validate()
