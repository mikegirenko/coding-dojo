"""
Given a positive integer N
Divisible by 3 → print “Fizz”
Divisible by 5 → print “Buzz”
Divisible by 3 and 5 → print “FizzBuzz”
Otherwise → print N
"""


def fizz_buzz(positive_integer):
    if positive_integer == 3:
        return "Fizz"
