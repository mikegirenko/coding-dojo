from args.code.program import MyProgram


def test_program_accepts_list_of_args():
    arguments_list = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyProgram(arguments_list)

    assert obj.accepted_arguments== arguments_list

def test_program_asks_for_value_of_specific_flag():
    specific_flag = "-p"
    expected_value = 8080
    arguments_list = {"-l": expected_value, "-p": 8080, "-d": "/usr/logs"}
    obj = MyProgram(arguments_list)
    value = obj.return_value_of_a_specific_flag(specific_flag)
    assert value == arguments_list["-l"]
