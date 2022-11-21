def find_prime_factors(input) -> list:
    prime_numbers = []
    prime_factors = []
    if input == 0 or input == 1:
        prime_numbers.append(0)
    if input >= 2:
        for i in range(1, input + 1):
            if find_prime_number(i):
                prime_numbers.append(i)
    if prime_numbers[0] == 0:
        prime_factors.append(0)
    if prime_numbers[0] != 0 and len(prime_numbers) == 1:
        if prime_numbers[0] == 2 and len(prime_numbers) == 1:
            prime_factors.append(2)
    if len(prime_numbers) > 1:
        for m in prime_numbers:
            if m * m == input:
                prime_factors.append(m)

    return prime_factors


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
