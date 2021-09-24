"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start - 1
        self.intial_start = start - 1

    def __repr__(self):
        return f"<SerialGenerator (start:{self.start})>"

    def generate(self):
        """increments serial number int by 1 and returns the new value"""
        self.start += 1
        return self.start

    def reset(self):
        """sets the serial number back to the original start int"""
        self.start = self.intial_start
