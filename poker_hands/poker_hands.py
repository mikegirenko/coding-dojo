from typing import List, Tuple, Any

INPUT_FILE = "poker_hands_input.txt"


def read_input_data(a_file) -> List[str]:
    with open(a_file, "r") as file:
        read_data = file.read()
    list_of_data = read_data.split("\n")

    return list_of_data


def prepare_hands_for_comparing(two_hands_of_cards) -> Tuple[Any, Any]:
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
    winner = ""
    winning_card = ""
    hand_one_values = []
    hand_two_values = []
    for card in hand_one:
        hand_one_values.append(card[:1])
    for card in hand_two:
        hand_two_values.append(card[:1])
    first_hand_just_cards_list = hand_one
    second_hand_just_cards_list = hand_two
    for i in range(len(first_hand_just_cards_list)):
        if first_hand_just_cards_list[i] != second_hand_just_cards_list[i]:
            if hand_one_values[i] > hand_two_values[i]:
                winner = player_one
                winning_card = str(hand_one_values[i])
            if hand_one_values[i] < hand_two_values[i]:
                winner = player_two
                winning_card = str(hand_one_values[i])
            game_result = winner + " wins. - with high card: " + winning_card
        else:
            game_result = "Tie"

    return game_result
