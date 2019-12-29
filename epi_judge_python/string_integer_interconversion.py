from test_framework import generic_test
from test_framework.test_failure import TestFailure
from icecream import ic


def int_to_string(x):
    if x == 0:
        return '0'
    d = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
         5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    s = ''
    neg = x < 0
    if neg:
        x = -x
    while x > 0:
        s = d[x % 10] + s
        x //= 10
    if neg:
        s = '-' + s
    return s


def string_to_int(s):
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
         '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    x = 0
    neg = False
    if s[0] == '-':
        neg = True
        s = s[1:]

    for letter in s:
        x = x * 10 + d[letter]

    if neg:
        x = -x
    return x

import functools
def string_to_int(s):
    return functools.reduce(lambda running_sum, c:
                            running_sum * 10 + int(c), 
                            s[s[0] == '-':], 0) * \
                            (-1 if s[0] == '-' else 1) # Add sign


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
