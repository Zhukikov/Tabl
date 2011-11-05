# Copyright (c) 2011 Andrejs Muzikovs
# This code is licensed under MIT license (see LICENSE for details)

"""Module to test tabl.py."""

import unittest

import tabl


class TestTabl(unittest.TestCase):
    """Unit test for tabl."""

    def test_empty_list(self):
        """Should print empty string."""
        tab = tabl.Tabl()
        string = tab.to_table([])
        self.assertEqual('', string)

    def test_single_element(self):
        """Should print single element."""
        tab = tabl.Tabl()
        string = tab.to_table([['abc']])
        self.assertEqual('+---+\n' + \
                         '|abc|\n' + \
                         '+---+\n', string)

    def test_three_elements(self):
        """Should print three elements in a row."""
        tab = tabl.Tabl()
        string = tab.to_table([['ab', 'c', 'def']])
        self.assertEqual('+--+-+---+\n' + \
                         '|ab|c|def|\n' + \
                         '+--+-+---+\n', string)

    def test_two_rows_equal_size(self):
        """Should print elements in two rows of equal size."""
        tab = tabl.Tabl()
        string = tab.to_table([['ab', 'c', 'def'], ['gh', 'i', 'jkl']])
        self.assertEqual('+--+-+---+\n' + \
                         '|ab|c|def|\n' + \
                         '+--+-+---+\n' + \
                         '|gh|i|jkl|\n' + \
                         '+--+-+---+\n', string)

    def test_two_rows_first_longer(self):
        """Should print two rows of equal size."""
        tab = tabl.Tabl()
        string = tab.to_table([['abb', 'c', 'def'], ['gh', 'i', 'jkl']])
        self.assertEqual('+---+-+---+\n' + \
                         '|abb|c|def|\n' + \
                         '+---+-+---+\n' + \
                         '|gh |i|jkl|\n' + \
                         '+---+-+---+\n', string)

    def test_add_up_to_rectangle(self):
        """Should put empty cells if empty elements."""
        tab = tabl.Tabl()
        string = tab.to_table([['a'], ['b', 'b']])
        self.assertEqual('+-+-+\n' + \
                         '|a| |\n' + \
                         '+-+-+\n' + \
                         '|b|b|\n' + \
                         '+-+-+\n', string)

    def test_custom_corners(self):
        """Should print table using custom corners."""
        tab = tabl.Tabl()
        tab.set_corner('*')
        string = tab.to_table([['a']])
        self.assertEqual('*-*\n' + \
                         '|a|\n' + \
                         '*-*\n', string)

    def test_disable_lines_split(self):
        """Should print elements without splitting them apart."""
        tab = tabl.Tabl()
        tab.split_lines(False)
        string = tab.to_table([['a', 'a'], ['b', 'b'], ['c', 'c']])
        self.assertEqual('+-+-+\n' + \
                         '|a|a|\n' + \
                         '+-+-+\n' + \
                         '|b|b|\n' + \
                         '|c|c|\n' + \
                         '+-+-+\n', string)

    def test_custom_ver_split(self):
        """Should print table using custom vertical split."""
        tab = tabl.Tabl()
        tab.set_ver('8')
        string = tab.to_table([['a']])
        self.assertEqual('+-+\n' + \
                         '8a8\n' + \
                         '+-+\n', string)

    def test_custom_hor_split(self):
        """Should print table using custom horizontal split."""
        tab = tabl.Tabl()
        tab.set_hor('~')
        string = tab.to_table([['a']])
        self.assertEqual('+~+\n' + \
                         '|a|\n' + \
                         '+~+\n', string)

    def test_add_up_to_rectangle_empty(self):
        """Should print cells of 0 size."""
        tab = tabl.Tabl()
        string = tab.to_table([['a', ''], ['']])
        self.assertEqual('+-++\n' + \
                         '|a||\n' + \
                         '+-++\n' + \
                         '| ||\n' + \
                         '+-++\n', string)

if __name__ == '__main__':
    unittest.main()
