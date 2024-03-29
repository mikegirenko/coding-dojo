from prime_factors.prime_factors import *


def test_find_prime_number():
    assert find_prime_number(2)
    assert find_prime_number(3)
    assert not find_prime_number(4)
    assert find_prime_number(5)
    assert find_prime_number(7)
    assert not find_prime_number(8)


def test_find_prime_factors():
    prime_factors = find_prime_factors(0)
    assert prime_factors[0] == 0
    prime_factors = find_prime_factors(1)
    assert prime_factors[0] == 0
    prime_factors = find_prime_factors(2)
    assert prime_factors[0] == 2
    prime_factors = find_prime_factors(3)
    assert prime_factors[0] == 3
    prime_factors = find_prime_factors(4)
    assert prime_factors[0] == 2
