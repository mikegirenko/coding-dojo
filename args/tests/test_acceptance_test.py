from args.code.program import MyProgram

"""
This is a Guiding test (or Acceptance test). It will pass when coding is done, but it is too
big to pass right away
"""

arguments_list = {"-l": False, "-p": 8080, "-d": "/usr/logs"}


def test_parse_arguments():
    obj = MyProgram(arguments_list)
    assert obj.accept_list_of_args() == arguments_list


def test_ask_for_one_argument():
    one_argument = "-l"
    obj = MyProgram(arguments_list)

    assert obj.return_one_argument_value() == arguments_list[one_argument]
