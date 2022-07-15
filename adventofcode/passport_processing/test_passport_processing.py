from adventofcode.passport_processing.passport_processing import *


def test_file_reading():
    assert len(read_file()) == 279


def test_clean_list():
    this_file = read_file()
    print(clean_list(this_file))  # not sure how assert that \n was removed


def test_has_all_required_fields_in_a_passport():
    this_file = "byr iyr eyr hgt hcl ecl pid cid"
    assert detect_required_fields_in_a_passport(this_file)


def test_does_not_have_all_required_fields_in_a_passport():
    this_file = "mmm iyr eyr hgt hcl ecl pid cid"
    assert not detect_required_fields_in_a_passport(this_file)


def test_cid_not_required_field():
    this_file = "byr iyr eyr hgt hcl ecl pid"
    assert detect_required_fields_in_a_passport(this_file)


def test_detect_which_passports_have_all_required_fields():
    this_file = read_file()
    clean_file = clean_list(this_file)
    assert detect_which_passports_have_all_required_fields(clean_file) == 213
