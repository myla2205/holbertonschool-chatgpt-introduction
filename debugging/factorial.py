#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) !=2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

try:
    f = factorial(num)
    print(f)
except ValueError as e:
    print(e)
    sys.exit(1)
