from typing import List, Dict

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]


def read_file() -> List[str]:
    with open("batch_file.txt", "r") as file:
        read_data = file.read()
    list_of_passwords = read_data.split("\n\n") # this is how I am splitting file on blank line

    return list_of_passwords


# this is to remove \n from each password which has a new line
def remove_n_from_password(list_of_passwords) -> List[str]:
    a_clean_list_of_passwords = []
    for i in list_of_passwords:
        i = i.replace("\n", " ")
        a_clean_list_of_passwords.append(i)

    return a_clean_list_of_passwords


def detect_required_fields_in_a_passport(one_passport) -> bool:
    has_required_fields = False
    valid_fields_counter = 0
    password_to_list = one_passport.split(" ")
    for field in required_fields:
        for item in password_to_list:
            if field in item and field != "cid":
                valid_fields_counter += 1
    if valid_fields_counter == 7:  # not counting "cid" as required
        has_required_fields = True

    return has_required_fields


def detect_which_passports_have_all_required_fields(file_with_passports):
    number_of_valid_passports = 0
    for passport in file_with_passports:
        if detect_required_fields_in_a_passport(passport):
            number_of_valid_passports += 1

    return number_of_valid_passports
