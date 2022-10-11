from poker_hands.poker_hands import read_input_data, INPUT_FILE, compare_two_hands, \
    prepare_hands_for_comparing, find_pair


def test_input_reading():
    print(read_input_data(INPUT_FILE))


def test_prepare_cards_for_comparing():
    two_hands = "Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH"
    _, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, _, hand_two = prepare_hands_for_comparing(two_hands)
    assert hand_one == ['2H', '3D', '5S', '9C', 'KD']
    assert hand_two == ['2D', '3H', '5C', '9S', 'KH']


def test_compare_hands_when_tie():
    two_hands = "Black: 2H 3D 5S 9C KD  White: 2H 3D 5S 9C KD"
    player_one, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, player_two, hand_two = prepare_hands_for_comparing(two_hands)

    assert compare_two_hands(player_one, hand_one, player_two, hand_two) == "Tie"


def test_compare_hands_when_highest_card_wins():
    two_hands = "Black: 2H 3D 5S 9C KD  White: 2C 3H 5S 8C KH"
    player_one, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, player_two, hand_two = prepare_hands_for_comparing(two_hands)

    assert compare_two_hands(player_one, hand_one, player_two, hand_two) == \
           "Black wins. - with high card: 9"


def test_compare_hands_when_pair_wins():
    two_hands = "Black: 2H 2D 5S 9C KD  White: 3C 3H 4S 8C KH"
    player_one, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, player_two, hand_two = prepare_hands_for_comparing(two_hands)

    assert compare_two_hands(player_one, hand_one, player_two, hand_two) == \
           "White wins. - with pair: 3"


def test_pair():
    cards = [2, 2, 4, 5]
    assert find_pair(cards) == [2]


def test_compare_hands_when_two_pairs_win():
    two_hands = "Black: 2H 2D 7S 7C KD  White: 3C 3H 4S 4C KH"  # B wins by pair of 7
    player_one, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, player_two, hand_two = prepare_hands_for_comparing(two_hands)

    assert compare_two_hands(player_one, hand_one, player_two, hand_two) == \
           "Black wins. - with pair: 7"


# Example
"""
Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH
Black: 2H 4S 4C 2D 4H  White: 2S 8S AS QS 3S
Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C KH
Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH
"""