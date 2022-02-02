import random


def one_try_score(): # one try (roll)
    number_of_pins_downed = random.randint(0, 10)
    return number_of_pins_downed


def one_frame_score():
    score_for_one_frame = 0 # here i keep running score
    try_one_score = one_try_score()
    #print("number_of_pins_try_one", number_of_pins_try_one)
    try_two_score = one_try_score()
    #print("number_of_pins_try_two", number_of_pins_try_two)
    # # need to see if its strike
    # if number_of_pins_try_one == 10:
    #     print("its a strike")
    #     # code goes here
    # else:
    #     number_of_pins_try_two = number_of_pins_downed_in_one_try()
    #     if number_of_pins_try_two == 10:
    #         print("its a spare")
    #         # code goes here
    # score_for_one_frame = number_of_pins_try_one + number_of_pins_try_two
    #print("score for one frame", score_for_one_frame)
    return try_one_score, try_two_score


def game_score():
    frame = 1
    score = 0
    while frame < 10: # always 10 frames
        try_one_score, _ = one_frame_score()
        _, try_two_score = one_frame_score()
        frame_score = try_one_score + try_two_score
        score += frame_score
        frame += 1
    return score, frame
