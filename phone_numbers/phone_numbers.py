from typing import List

INPUT_FILE = "phone_data.txt"


def read_input_data(a_file) -> List[str]:
    with open(a_file, "r") as file:
        read_data = file.read()
    list_of_data = read_data.split("\n")

    return list_of_data


def list_of_first_three_digits(list_of_numbers) -> List:
    list_of_split_numbers = []
    list_of_first_three_digits = []
    for number in list_of_numbers:
        split_number = number.split(",")
        list_of_split_numbers.append(split_number[1])
    for number in list_of_split_numbers:
        list_of_first_three_digits.append(number[:3])

    return list_of_first_three_digits


def determine_consistency(this_list) -> bool:
    dups = []
    uniqs = []
    consistent_list = True
    for i in this_list:
        if i not in uniqs:
            uniqs.append(i)
        else:
            dups.append(i)
            consistent_list = False
    return consistent_list


if __name__ == "__main__":
    all_data = read_input_data(INPUT_FILE)
    list_of_numbers = list_of_first_three_digits(all_data)
    is_this_list_consistent = determine_consistency(list_of_numbers)
    print("The answer is", is_this_list_consistent)
