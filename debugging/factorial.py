#!/usr/bin/python3
import sys


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # decrement n to avoid infinite loop
    return result


if len(sys.argv) != 2:
    print("usage: python factorial.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        raise ValueError("factorial is not define for negative numbes.")
except ValueError:
    print("Error:")
    sys.exit(1)

f = factorial(number)
print(f)
