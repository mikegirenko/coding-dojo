from poker_hands.poker_hands import read_input_data, INPUT_FILE, compare_two_pairs, \
    prepare_cards_for_comparing


def test_input_reading():
    print(read_input_data(INPUT_FILE))


def test_prepare_cards_for_comparing():
    two_pairs = "Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH"
    pair_one, _ = prepare_cards_for_comparing(two_pairs)
    _, pair_two = prepare_cards_for_comparing(two_pairs)
    assert pair_one == ['2H', '3D', '5S', '9C', 'KD']
    assert pair_two == ['2D', '3H', '5C', '9S', 'KH']


def test_compare_pairs_when_tie():
    two_pairs = "Black: 2H 3D 5S 9C KD  White: 2H 3D 5S 9C KD"
    pair_one, _ = prepare_cards_for_comparing(two_pairs)
    _, pair_two = prepare_cards_for_comparing(two_pairs)

    assert compare_two_pairs(pair_one, pair_two) == "Tie"
