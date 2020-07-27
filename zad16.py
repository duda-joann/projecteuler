"""
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?

"""


def count_numbers():
    number = str(2**1000)
    numbers = [int(i) for i in number]
    sum_of_digits = sum(numbers)
    return sum_of_digits


if __name__ == '__main__':
    print(count_numbers())
