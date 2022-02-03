import random


def one_try_score():  # one try (roll)
    number_of_pins_downed = random.randint(0, 10)
    return number_of_pins_downed


def one_frame_score():  # one frame, two tries (rolls)
    try_one_score = one_try_score()
    try_two_score = one_try_score()
    return try_one_score, try_two_score


def game_score():
    frame = 1
    game_score_final = 0
    while frame < 10:  # always 10 frames
        try_one_score, _ = one_frame_score()
        _, try_two_score = one_frame_score()
        if try_one_score == 10:
            print("First try", "and try score is", try_one_score)
        frame_score = try_one_score + try_two_score
        if frame_score == 10:
            print("Frame is", frame, "and frame score is", frame_score)
        game_score_final += frame_score
        print("Game score is", game_score_final)
        frame += 1
    return game_score_final
