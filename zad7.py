"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

import math


def is_prime(number: int) -> bool:
    """
    :param number:
    :return:  check if number is prime
    """

    if all(number % i != 0 for i in range(2, int(math.sqrt(number) +1))):
        return True


def find_nth_prime(border: int) -> int:
    """
    :param border: -nth  number which is prime
    :return: return search prime number

    """
    amount = 6
    prime = 13
    number = 14
    while amount < border:
        if is_prime(number):
            prime = number
            amount += 1
        number += 1

    if amount == border:
        return prime




if __name__ == '__main__':
    a = find_nth_prime(10001)
    print(a)