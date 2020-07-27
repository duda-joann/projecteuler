"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
 numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrom_product(number: int) -> bool:
    return str(number) == str(number)[::-1]


def find_largest_palindrom(number: int) -> int:

    palindrom_product = 0
    number = 999
    for i in range(999, 100, -1):
        for number in range(999, 100, -1):
            p = i * number
            if is_palindrom_product(p) and p > palindrom_product:
                palindrom_product = p

    return palindrom_product


if __name__ == '__main__':
    number = find_largest_palindrom(1000)
    print(number)