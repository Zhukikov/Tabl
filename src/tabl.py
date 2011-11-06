# Copyright (c) 2011 Andrejs Muzikovs
# This code is licensed under MIT license (see LICENSE for details)

"""Tabl module."""


class Tabl:
    """Class which converts lists to tables."""

    def __init__(self):
        """Initialization."""
        self.corner = '+'
        self.ver = '|'
        self.hor = '-'
        self.split = True

    def split_lines(self, boolean):
        """Split lines or not."""
        self.split = boolean

    def set_corner(self, char):
        """Set corner character."""
        self.corner = char

    def set_ver(self, char):
        """Set vertical split character."""
        self.ver = char

    def set_hor(self, char):
        """Set horizontal split character."""
        self.hor = char

    def to_table(self, lis):
        """Convert list to table."""
        result = ''
        if len(lis) > 0:
            sizes = self._get_max_cell_sizes(lis)
            result += self._print_hor_div(sizes)
            for row in range(len(lis)):
                result += self._print_row(lis[row], sizes)
                if row == 0 or row == len(lis) - 1 or self.split == True:
                    result += self._print_hor_div(sizes)
        return result

    def _get_max_cell_sizes(self, lis):
        """Get a list with maximum cell size in each column."""
        result = []

        for i in range(len(lis)):
            for j in range(len(lis[i])):
                if len(result) < j + 1:
                    result += [0]
                if result[j] < len(str(lis[i][j])):
                    result[j] = len(str(lis[i][j]))
        return result

    def _print_hor_div(self, row):
        """Print horizontal line."""
        if len(row) == 0:
            return ''
        result = self.corner
        for char in row:
            result += self.hor * char + self.corner
        result += '\n'
        return result

    def _print_row(self, row, sizes):
        """Print one table row."""
        result = ''
        for i in range(len(sizes) - len(row)):
            row += ['']
        el_count = len(row)

        if el_count > 0:
            result += self.ver
            for i in range(el_count):
                result += str(row[i])
                result += ' ' * (sizes[i] - len(str(row[i])))
                result += self.ver
            result += '\n'

        return result
