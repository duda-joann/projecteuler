"""
Problem 6
The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def find_sum(number: int) -> int:
    return sum(element**2 for element in range(0, number + 1))

def find_square(number) -> int:
    return (sum(element for element in range(0, number + 1)))**2


def find_difference(number):
    return find_square(number) - find_sum(number)


if __name__ == '__main__':
    result = find_difference(100)
    print(result)