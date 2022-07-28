from typing import List


def read_input() -> List[str]:
    with open("years_list.txt", "r") as file:
        read_data = file.read()
    years = read_data.split("\n")

    return years


def determine_if_year_is_leap_year(year_to_check) -> bool:
    is_leap = False
    if year_to_check % 4 == 0:
        if year_to_check % 100 != 0 or year_to_check % 400 == 0:
            is_leap = True

    return is_leap


def which_year_is_leap() -> List[str]:
    years = read_input()
    leap_years = []
    for year in years:
        if determine_if_year_is_leap_year(int(year)):
            leap_years.append(year)

    return leap_years
