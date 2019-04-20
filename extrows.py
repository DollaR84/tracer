"""
Extended rows module.

Created on 20.04.2019

@author: Ruslan Dolovanyuk

"""


class ExtRow:
    """Extended row class."""

    def __init__(self, row, num):
        """Initialise extended row class."""
        self.row = row
        self.num = num
        self.hide = False
        self.prev = None
        self.next = None


class ExtRows:
    """Extended rows class."""

    def __init__(self, row):
        """Initialise extended rows class."""
        self.head = ExtRow(row, 0)
        self.last = self.head

    def add(self, row):
        """Add new ExtRow."""
        self.last.next = ExtRow(row, self.last.num+1)
        self.last.next.prev = self.last
        self.last = self.last.next
