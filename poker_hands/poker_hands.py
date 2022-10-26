from typing import List

INPUT_FILE = "poker_hands_input.txt"


def read_input_data(a_file) -> List[str]:
    with open(a_file, "r") as file:
        read_data = file.read()
    list_of_data = read_data.split("\n")

    return list_of_data


def prepare_hands_for_comparing(two_hands_of_cards):
    two_pairs_split = two_hands_of_cards.split("  ")
    first_pair = two_pairs_split[0]
    second_pair = two_pairs_split[1]
    first_player = first_pair[:5]
    second_player = second_pair[:5]
    first_pair_just_cards_list = first_pair[7:]
    second_pair_just_cards = second_pair[7:]
    hand_of_cards_one = first_pair_just_cards_list.split(" ")
    hand_of_cards_two = second_pair_just_cards.split(" ")

    return first_player, hand_of_cards_one, second_player, hand_of_cards_two


# Compare TWO pairs of poker hands to indicate which has higher rank
def compare_two_hands(player_one, hand_one, player_two, hand_two) -> str:
    game_result = ""
    hand_one_values = []
    hand_two_values = []
    for card in hand_one:
        hand_one_values.append(card[:1])
    for card in hand_two:
        hand_two_values.append(card[:1])
    hand_one_suits = []
    hand_two_suits = []
    for card in hand_one:
        hand_one_suits.append(card[-1])
    for card in hand_two:
        hand_two_suits.append(card[-1])
    first_hand_just_cards_list = hand_one
    second_hand_just_cards_list = hand_two
    if find_repeated_card(hand_one_values) and find_repeated_card(hand_two_values):   # Pairs
        hand_one_pair = find_repeated_card(hand_one_values)
        hand_two_pair = find_repeated_card(hand_two_values)
        hand_one_pair_max = max(hand_one_pair)
        hand_two_pair_max = max(hand_two_pair)
        if len(hand_one_pair) == 2 and len(hand_two_pair) == 2:     # One Pair
            if hand_one_pair > hand_two_pair:
                winner = player_one
                winning_card = hand_one_pair[0]
                game_result = winner + " wins. - with pair: " + winning_card
            else:
                winner = player_two
                winning_card = hand_two_pair[0]
                game_result = winner + " wins. - with pair: " + winning_card
        if len(hand_one_pair) == 4 and len(hand_two_pair) == 4:     # Two Pairs
            if hand_one_pair_max > hand_two_pair_max:
                winner = player_one
                winning_card = hand_one_pair_max
                game_result = winner + " wins. - with pair: " + winning_card
            else:
                winner = player_two
                winning_card = hand_two_pair_max
                game_result = winner + " wins. - with pair: " + winning_card
        if len(hand_one_pair) == 3 and len(hand_two_pair) == 3:     # Three of a kind
            if hand_one_pair_max > hand_two_pair_max:
                winner = player_one
                winning_card = hand_one_pair_max
                game_result = winner + " wins. - with pair: " + winning_card
            else:
                winner = player_two
                winning_card = hand_two_pair_max
                game_result = winner + " wins. - with pair: " + winning_card
    if find_if_consecutive(hand_one_values) and find_if_consecutive(hand_two_values):  # Straight
        if max(hand_one_values) > max(hand_two_values):
            winner = player_one
            game_result = winner + " wins. - by higher straight"
        else:
            winner = player_two
            game_result = winner + " wins. - by higher straight"
    # Flash logic
    if len(set(hand_one_suits)) == 1:
        winner = player_one
        game_result = winner + " wins. - by flash"
    if len(set(hand_two_suits)) == 1:
        winner = player_two
        game_result = winner + " wins. - by flash"
    # Full House logic
    if find_full_house(hand_one_values):
        winner = player_one
        game_result = winner + " wins. - by full house"
    if find_full_house(hand_two_values):
        winner = player_two
        game_result = winner + " wins. - by full house"
    if not find_repeated_card(hand_one_values) or not find_repeated_card(hand_two_values):
        if not find_if_consecutive(hand_one_values) or not find_if_consecutive(hand_two_values):
            if not len(set(hand_one_suits)) == 1:
                if not find_full_house(hand_one_values):
                    for i in range(len(first_hand_just_cards_list)):
                        if first_hand_just_cards_list[i] != second_hand_just_cards_list[i]:  # Not a Tie
                            if hand_one_values[i] > hand_two_values[i]:         # High Card
                                winner = player_one
                                winning_card = str(hand_one_values[i])
                                game_result = winner + " wins. - with high card: " + winning_card
                            if hand_one_values[i] < hand_two_values[i]:         # High Card
                                winner = player_two
                                winning_card = str(hand_one_values[i])
                                game_result = winner + " wins. - with high card: " + winning_card
                        else:
                            game_result = "Tie"                                 # Tie

    return game_result


def find_repeated_card(hand_of_cards) -> List:
    repeated_cards = [card for card in hand_of_cards if hand_of_cards.count(card) > 1]

    return repeated_cards


def find_if_consecutive(hand_of_cards):
    consecutive = False
    i = 0
    while i < len(hand_of_cards) - 1:
        first = int(hand_of_cards[i])
        second = int(hand_of_cards[i + 1])
        if first + 1 == second:
            consecutive = True
        else:
            return consecutive
        i += 1

    return consecutive


def find_full_house(hand_of_cards):
    full_house = False
    uniques = set(hand_of_cards)
    list_of_uniques = list(uniques)
    if (hand_of_cards.count(list_of_uniques[0]) == 3 and hand_of_cards.count(list_of_uniques[1]) == 2) or\
            (hand_of_cards.count(list_of_uniques[1]) == 3 and hand_of_cards.count(list_of_uniques[0]) == 2):
        full_house = True

    return full_house

# TODO continue with Four of a Kind logic
