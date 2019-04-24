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

    def get_hide_before(self, elem):
        """Return the sum hide rows with before list to element."""
        result = 0
        while elem is not None:
            if elem.hide:
                result += 1
            elem = elem.prev
        return result

    def change(self, subrow, hide):
        """Hide or show row which included subrow."""
        elem = self.head
        while elem is not None:
            if elem.row.find(subrow) != -1:
                elem.hide = hide
            elem = elem.next

    def get_rows(self):
        """Return all show rows."""
        rows = []
        elem = self.head
        while elem is not None:
            if not elem.hide:
                rows.append(elem.row)
            elem = elem.next
        return ''.join(rows)
