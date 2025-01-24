#!/usr/bin/python3
#!/usr/bin/python3
import sys

"""
       Compute the factorial of a non-negative integer n.

       Parameters:
       n (int): A non-negative integer whose factorial is to be computed.

       Returns:
       int: The factorial of the given integer n.

       Raises:
       ValueError: If n is negative, as factorial is not defined for negative numbers.
       """


def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <non-negative integer>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError("Negative integers are not allowed.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    result = factorial(num)
    print(result)


if __name__ == "__main__":
    main()
