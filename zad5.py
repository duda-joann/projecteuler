from math import sqrt

"""
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def find_NWW(numbers):
    product_of_primes = 1
    primes = []

    for i in range(2, numbers +1):
        for d in range(2, int(sqrt(i) +1)):
            if i % d == 0:
                break
        else:
            primes.append(i)

    for number in primes:
        product_of_primes *= number

    factor = 1
    while True:
        if any(factor * product_of_primes % i != 0 for i in range(numbers // 2, numbers + 1)):
            factor += 1
        else:
            return factor * product_of_primes


if __name__ == '__main__':
    my_NWW = find_NWW(20)
    print(my_NWW)

