# Tabl v0.2.1

Tabl converts a list of lists to a table using ASCII art.
Different customization options are supported, which help
achieve the desired output.

Licensed under MIT license (see LICENSE for details).

## Basic usage

    >>> import tabl
    >>>
    >>> t = tabl.Tabl()
    >>> result = t.to_table([['Name', 'Phone number'],
    ...                      ['Andrejs', '1234567'],
    ...                      ['Laura']])
    >>>
    >>> print(result)
    +-------+------------+
    |Name   |Phone number|
    +-------+------------+
    |Andrejs|1234567     |
    +-------+------------+
    |Laura  |            |
    +-------+------------+

## Authors

Andrejs Muzikovs <andrejs.muzikovs@gmail.com>
