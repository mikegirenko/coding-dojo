import random


def number_of_pins_downed_in_one_try():
    number_of_pins_downed = random.randint(0, 10)
    return number_of_pins_downed


def number_of_pins_downed_in_one_frame():
    number_of_pins_downed = []
    for i in range(0, 2):
        number_of_pins_downed.append(number_of_pins_downed_in_one_try())
    return number_of_pins_downed


def score_for_one_frame():
    number_of_pins = number_of_pins_downed_in_one_frame()
    try_one = number_of_pins[0]
    try_two = number_of_pins[1]
    score = try_one + try_two
    return score


def game_score():
    frame = 1
    score = 0
    while frame < 11:
        score += score_for_one_frame()
        frame += 1
    return score

