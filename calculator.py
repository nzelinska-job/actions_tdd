# calculator.py


class Calculator:
    """A simple calculator class."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        """Return a raised to the power of b."""
        return a**b

    def check_negative(self, a):
        """Check if a number is negative.

        Returns:
            bool: True if a is negative, False otherwise.
        """
        return a < 0

    def sqrt(self, a):
        """Return the square root of a.

        Raises:
            ValueError: If a is negative.
        """
        if self.check_negative(a):
            raise ValueError("Cannot take the square root of a negative number")
        return a**0.5
