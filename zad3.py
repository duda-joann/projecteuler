"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt


def find_primes(number: int) -> list:
    """ function which  finds all primes less than square
     root of  number, which can be a factor of request number
     :param: number provide for  user
     :return: list of primes

     """
    square_of_number = sqrt(number)
    lista = [i for i in range(2, int(square_of_number) + 2) if i % 2 != 0]
    factor = 2
    for number in lista:
        if number * factor in lista:
            number = 1
        else:
            factor += 1

    return lista


def find_the_largest_prime_factor(number: int)-> int:
    """

    :param number: user's input which is number
    :return: the largest prime factor
    """
    primes = find_primes(number)
    factor = 0
    for element in primes:
        if number % element and element > factor:
            factor = element

    return factor


if __name__ == '__main__':
    the_largest_factor = (find_the_largest_prime_factor(600851475143))
    print(the_largest_factor)
