"""

Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from math import sqrt


class Number:

    def __init__(self, number: int):
        self.number = number

    def find_primes(self):
        primes = [i for i in range(2, self.number) if all(int(i) % d != 0 for d in range(2, int(sqrt(i))+ 1))]
        return primes

    def sum_primes(self):
        return sum(self.find_primes())


if __name__ == '__main__':
    number = 2000000
    sum_all_primes = Number(number).sum_primes()
    print(sum_all_primes)


