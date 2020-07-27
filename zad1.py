"""
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""


def find_sum(number: int) -> int:
    total = 0
    for i in range(number):
        if i % 15 == 0:
            total += i
        elif i % 3 == 0:
            total += i
        elif i % 5 == 0:
            total += i

    return total


if __name__ == '__main__':
    a = find_sum(1000)
    print(a)
