"""
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""


def factorial(n:int) -> int:
    if n == 1:
        silnia = 1
    else:
        silnia = n * factorial(n-1)

    return silnia


def count_sum_of_digits(number: int) -> int:
    digits = [int(i) for i in str(number)]
    sum_of_digits = sum(digits)
    return sum_of_digits


if __name__ == '__main__':
    a = factorial(100)
    print(a)
    print(count_sum_of_digits(a))

