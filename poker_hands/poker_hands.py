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
    first_hand_just_cards_list = hand_one
    second_hand_just_cards_list = hand_two

    if pair(hand_one_values) and pair(hand_two_values):
        hand_one_pair = pair(hand_one_values)
        hand_two_pair = pair(hand_two_values)
        if hand_one_pair > hand_two_pair:
            winner = player_one
            winning_card = hand_one_pair[0]
            game_result = winner + " wins. - with pair: " + winning_card
        else:
            winner = player_two
            winning_card = hand_two_pair[0]
            game_result = winner + " wins. - with pair: " + winning_card

    if not pair(hand_one_values) or not pair(hand_two_values):
        for i in range(len(first_hand_just_cards_list)):
            if first_hand_just_cards_list[i] != second_hand_just_cards_list[i]:  # Not a Tie
                if hand_one_values[i] > hand_two_values[i]:  # High Card
                    winner = player_one
                    winning_card = str(hand_one_values[i])
                    game_result = winner + " wins. - with high card: " + winning_card
                if hand_one_values[i] < hand_two_values[i]:  # High Card
                    winner = player_two
                    winning_card = str(hand_one_values[i])
                    game_result = winner + " wins. - with high card: " + winning_card
            else:
                game_result = "Tie"  # Tie

    return game_result


def pair(hand_of_cards): # find if hand has pair
    duplicates = []
    seen = set()
    for card in hand_of_cards:
        if card in seen:
            duplicates.append(card)
        else:
            seen.add(card)

    return duplicates

 # TODO continue with two Pairs logic
