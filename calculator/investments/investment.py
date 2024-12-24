"""
investment.py

This module contains the base implementation of investment
"""

from calculator.investments.exceptions import (
    InvalidInvestmentType,
    InvalidInvestmentTime,
    InvalidInvestmentReturns,
    InvalidInvestmentAmount,
)


class Investment:
    """This is base implementation of Investment"""

    def __init__(self, amount: float, rate: float, time: int):
        """Initialize investment

        Args:
            amount (float): investment amount
            rate (float): returns rate of intrest
            time (int): time in years
        """
        self._amount = amount
        self._time = time
        self._rate = rate
        self._investment_type = "Monthly"

    @property
    def investment_type(self) -> str:
        """This property gets the investment type"""
        return self._investment_type

    @investment_type.setter
    def investment_type(self, value) -> None:
        self._investment_type = value

    @property
    def amount(self) -> float:
        """
        Property for amount
        """
        return self._amount

    @property
    def rate(self) -> float:
        """Property for rate

        Returns:
            float: returns rate
        """
        return self._rate

    @property
    def time(self) -> int:
        """Property for time

        Returns:
            int: time in years
        """
        return self._time

    def validate(self) -> bool:
        """
        This method validates investments

        Returns: True for valid investments

        Raises:
            InvalidInvestemtType
            InvalidInvestemtAmount
            InvalidInvestemtRate
            InvalidInvestemtTime
        """
        if self.investment_type not in ["Monthly", "Yearly"]:
            raise InvalidInvestmentType
        if self.amount <= 0:
            raise InvalidInvestmentAmount
        if self.rate <= 0:
            raise InvalidInvestmentReturns
        if self.time <= 0:
            raise InvalidInvestmentTime

    def calculate(self) -> float:
        """This method will return the total value
        post investment

        Returns:
            float: total value post investment
        """
        pass
