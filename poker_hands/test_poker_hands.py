from poker_hands.poker_hands import read_input_data, INPUT_FILE, compare_two_hands, \
    prepare_hands_for_comparing, find_repeated_card, find_if_consecutive, find_full_house


def test_input_reading():
    print(read_input_data(INPUT_FILE))


def test_prepare_cards_for_comparing():
    two_hands = "Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH"
    _, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, _, hand_two = prepare_hands_for_comparing(two_hands)
    assert hand_one == ['2H', '3D', '5S', '9C', 'KD']
    assert hand_two == ['2D', '3H', '5C', '9S', 'KH']


def test_compare_hands_when_tie():
    two_hands = "Black: 1H 3D 5S 9C KD  White: 1H 3D 5S 9C KD"
    player_one, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, player_two, hand_two = prepare_hands_for_comparing(two_hands)

    assert compare_two_hands(player_one, hand_one, player_two, hand_two) == "Tie"


def test_compare_hands_when_highest_card_wins():
    two_hands = "Black: 1H 3D 5S 9C KD  White: 1C 3H 5S 8C KH"
    player_one, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, player_two, hand_two = prepare_hands_for_comparing(two_hands)

    assert compare_two_hands(player_one, hand_one, player_two, hand_two) == \
           "Black wins. - with high card: 9"


def test_find_repeated_card_no_card():
    cards = [1, 0, 2, 4, 5]
    repeats = find_repeated_card(cards)
    assert repeats == []


def test_find_repeated_card_two_cards():
    cards = [2, 3, 2, 4, 5]
    repeats = find_repeated_card(cards)
    assert repeats == [2, 2]


def test_find_repeated_card_three_card():
    cards = [2, 2, 2, 4, 5]
    repeats = find_repeated_card(cards)
    assert repeats == [2, 2, 2]


def test_find_repeated_card_two_cards_twice():
    cards = [2, 2, 3, 3, 5]
    repeats = find_repeated_card(cards)
    assert repeats == [2, 2, 3, 3]


def test_compare_hands_when_pair_wins():
    two_hands = "Black: 2H 2D 5S 9C KD  White: 3C 3H 4S 8C KH"
    player_one, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, player_two, hand_two = prepare_hands_for_comparing(two_hands)

    assert compare_two_hands(player_one, hand_one, player_two, hand_two) == \
           "White wins. - with pair: 3"


def test_compare_hands_when_two_pairs_win():
    two_hands = "Black: 2H 2D 7S 7C KD  White: 3C 3H 4S 4C KH"  # B wins by pair of 7
    player_one, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, player_two, hand_two = prepare_hands_for_comparing(two_hands)

    assert compare_two_hands(player_one, hand_one, player_two, hand_two) == \
           "Black wins. - with pair: 7"


def test_compare_hands_when_three_of_kind_wins():
    two_hands = "Black: 9H 9D 9S 7C KD  White: 3C 3H 3S 4C KH"  # B wins by three 9s
    player_one, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, player_two, hand_two = prepare_hands_for_comparing(two_hands)

    assert compare_two_hands(player_one, hand_one, player_two, hand_two) == \
           "Black wins. - with pair: 9"


def test_compare_hands_when_straight_wins():
    two_hands = "Black: 5H 6D 7S 8C 9D  White: 2C 3H 4S 5C 6H"  # B wins by higher straight
    player_one, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, player_two, hand_two = prepare_hands_for_comparing(two_hands)

    assert compare_two_hands(player_one, hand_one, player_two, hand_two) == \
           "Black wins. - by higher straight"


def test_hand_has_consecutive_values():
    hand = [5, 6, 7, 8, 9]
    consecutive = find_if_consecutive(hand)

    assert consecutive


def test_hand_does_not_have_consecutive_values():
    hand = [10, 6, 7, 8, 9]
    consecutive = find_if_consecutive(hand)

    assert not consecutive


def test_hand_consecutive_what():
    hand = [5, 6, 7, 8, 9]
    consecutive = find_if_consecutive(hand)

    assert consecutive


def test_compare_hands_when_flash_wins():
    two_hands = "Black: 1H 6H 8H 10H KH  White: 2C 3H 4S 5C 6H"  # B wins by flash
    player_one, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, player_two, hand_two = prepare_hands_for_comparing(two_hands)

    assert compare_two_hands(player_one, hand_one, player_two, hand_two) == \
           "Black wins. - by flash"


def test_compare_hands_when_full_house_wins():
    two_hands = "Black: 1D 9H 1C 9H 1H  White: 2C 3H 4S 5C 6H"  # B wins by full house
    player_one, hand_one, _, _ = prepare_hands_for_comparing(two_hands)
    _, _, player_two, hand_two = prepare_hands_for_comparing(two_hands)

    assert compare_two_hands(player_one, hand_one, player_two, hand_two) == \
           "Black wins. - by full house"


def test_find_full_house():
    hand = [1, 10, 1, 10, 1]
    assert find_full_house(hand)
