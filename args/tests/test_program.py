from args.code.program import MyProgram
from args.code.parser import MyParser


def test_program_accepts_list_of_args():
    arguments_list = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyProgram(arguments_list)

    assert obj.accept_list_of_args() == arguments_list


def test_program_passes_arguments_to_parser(): # TODO continue here
    schema = ["-l", "-p", "-d"]
    arguments_list = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyProgram(arguments_list)
    obj.pass_arguments_to_parser()



def test_make_schema():
    arguments_list = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    expected_schema = ['-l', '-p', '-d']
    obj = MyProgram(arguments_list)
    assert obj.make_schema() == expected_schema


def test_program_asks_for_value_of_specific_flag():
    specific_flag = "-l"
    arguments_list = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyProgram(arguments_list)
    value = obj.return_one_flag_value(specific_flag)
    assert value == arguments_list["-l"]
