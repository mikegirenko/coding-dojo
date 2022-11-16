"""
"Prime Factorization" is finding which prime numbers multiply together to make the
original number
"""
# get input, for every integer in the input check if this integer is a prime number
# divide input by prime number = does it equal to another prime number?
# prime numbers are 2, 3, 5, 7, 11


def find_prime_factors(input) -> list:
    prime_numbers = []
    prime_factors = []
    if input == 0 or input == 1:
        prime_numbers.append(0)
    if input >= 2:
        for i in range(1, input + 1):
            if find_prime_number(i):
                prime_numbers.append(i)
        print("prime_numbers", prime_numbers)
        # i = 2
        # while i <= len(prime_numbers):
        #     if input % prime_numbers[i] == 2:
        #         prime_factors.append(prime_numbers[i])
        # print("prime factors")

    return prime_numbers


def find_prime_number(number):
    flag = False
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                flag = False
                break
        else:
            flag = True

    return flag
