from phone_numbers.phone_numbers import read_input_data, INPUT_FILE, \
    list_of_first_three_digits, determine_consistency


def test_read_input_data():
    print(read_input_data(INPUT_FILE))


def test_list_of_first_three_digits():
    list_of_numbers = ["Kimberlee Turlington,039 298-72-30",
                       "Miguel Eveland,039-2659094",
                       "Audrie Smid,03758295-10 32"]
    print(list_of_first_three_digits(list_of_numbers))


def test_inconsistent_list():
    list_of_prefix = ['039', '039', '037', '4']
    is_consistent = determine_consistency(list_of_prefix)
    assert not is_consistent


def test_consistent_list():
    list_of_prefix = ['039', '1', '037', '4']
    is_consistent = determine_consistency(list_of_prefix)
    assert is_consistent
