import math
"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    listOfPrimes = []
    number = 2
    while (len(listOfPrimes) < number_of_primes):
        check = True
        for a in range(1, math.ceil(number**0.5) + 1):
            if a == 1 or a == number:
                continue
            if (number%a == 0):
                check = False
        if check:
            listOfPrimes.append(number)
        number += 1
    return listOfPrimes

