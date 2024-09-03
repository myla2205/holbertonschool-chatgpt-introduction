#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to eventually end the loop
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <positive_integer>")
        return

    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Input must be a positive integer")
        print(factorial(number))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

