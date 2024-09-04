#!/usr/bin/python3
import sys

"""
factorial - Computes the factorial of a non-negative integer.

Parameter:
n (int): The non-negative integer for which to compute the factorial.

Returns:
int: The factorial of the input integer.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
