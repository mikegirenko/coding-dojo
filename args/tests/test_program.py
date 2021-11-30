from args.code.program import MyProgram
from args.code.parser import MyParser


def test_program_accepts_list_of_args():
    list_1 = [1,2]
    obj = MyProgram(list_1)

    assert obj.accept_list_of_args() == list_1


def test_program_passes_arguments_to_parser():
    schema = ["-l", "-p", "-d"]
    arguments_list = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyParser(schema, arguments_list)

    assert obj.return_accepted_schema()


def test_program_asks_for_value_of_specific_flag():
    specific_flag = "-l"
    arguments_list = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyProgram(arguments_list)
    value = obj.return_one_flag_value(specific_flag)
    assert value == arguments_list["-l"]
