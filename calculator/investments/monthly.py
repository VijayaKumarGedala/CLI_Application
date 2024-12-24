"""
monthly.py

This module contains monthly investment type calculations
"""

from calculator.investments.investment import Investment


class MonthlyInvestment(Investment):
    """This class contains monthly investment cacluator"""

    def calculate(self) -> float:
        """This method will calculate monthly investment returns

        Raises:
            InvalidInvestemtType
            InvalidInvestemtAmount
            InvalidInvestemtRate
            InvalidInvestemtTime
        """
        self._investment_type = "Monthly"
        self.validate()
        months = self.time * 12
        yearly_returns = self.rate / 100
        returns = yearly_returns / 12
        total_amount = (
            self.amount * (((1 + returns) ** months - 1) / returns) * (1 + returns)
        )
        return total_amount
