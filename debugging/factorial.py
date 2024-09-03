#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to eventually end the loop
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <positive_integer>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Input must be a positive integer")
    except ValueError as e:
        print(e)
        sys.exit(1)

    f = factorial(number)
    print(f)

if __name__ == "__main__":
    main()
