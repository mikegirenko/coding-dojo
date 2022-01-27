import random


def number_of_pins_downed_in_one_try():
    number_of_pins_downed = random.randint(0, 10)
    return number_of_pins_downed


def score_for_one_frame():
    running_score = 0 # here i keep running score
    number_of_pins_try_one = number_of_pins_downed_in_one_try()
    number_of_pins_try_two = 0
    # need to see if its strike
    if number_of_pins_try_one == 10:
        print("its a strike")
        # code goes here
    else:
        number_of_pins_try_two = number_of_pins_downed_in_one_try()
        if number_of_pins_try_two == 10:
            print("its a spare")
            # code goes here
    running_score = number_of_pins_try_one + number_of_pins_try_two
    return running_score


def game_score():
    frame = 1
    score = 0
    while frame < 11: # always 10 frames
        score += score_for_one_frame()
        frame += 1
    return score
