from typing import List, Tuple, Any

INPUT_FILE = "poker_hands_input.txt"


def read_input_data(a_file) -> List[str]:
    with open(a_file, "r") as file:
        read_data = file.read()
    list_of_data = read_data.split("\n")

    return list_of_data


def prepare_cards_for_comparing(two_pairs_of_cards) -> Tuple[Any, Any]:
    two_pairs_split = two_pairs_of_cards.split("  ")
    first_pair = two_pairs_split[0]
    second_pair = two_pairs_split[1]
    first_pair_just_cards_list = first_pair[7:]
    second_pair_just_cards = second_pair[7:]
    cards_one = first_pair_just_cards_list.split(" ")
    cards_two = second_pair_just_cards.split(" ")

    return cards_one, cards_two


# Compare TWO pairs of poker hands to indicate which has higher rank
def compare_two_pairs(pair_one, pair_two):
    result = ""
    first_pair_just_cards_list = pair_one
    second_pair_just_cards_list = pair_two
    for i in range(len(first_pair_just_cards_list)):
        if first_pair_just_cards_list[i] != second_pair_just_cards_list[i]:
            result = "No Tie" # remove
            return
        else:
            result = "Tie"
    return result
