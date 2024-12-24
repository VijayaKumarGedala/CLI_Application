"""
lumpsum.py

This module contains lumpsum investment calculator
"""

from calculator.investments.investment import Investment


class LumpsumInvestment(Investment):
    """
    This class is used for Lumpsump Investments
    """

    def calculate(self) -> float:
        """
        This method calculates lumpsum investments

        Raises:
            InvalidInvestemtType
            InvalidInvestemtAmount
            InvalidInvestemtRate
            InvalidInvestemtTime
        """
        self._investment_type = "Yearly"
        self.validate()
        returns = self.rate / 100
        total_amount = self.amount * (1 + returns) ** self.time
        return total_amount
