from args.code.parser import MyParser


class MyProgram:
    def __init__(self, arguments):
        self.accepted_arguments = {}
        self.accepted_arguments = arguments
        self.schema = ["-l", "-p", "-d"]
        self.parser = MyParser(self.schema, self.accepted_arguments)

    def return_value_of_a_specific_flag(self, one_argument_flag):
        value = None
        if self.parser.list_matches_schema:
            for flag in self.parser.arguments.keys():
                if flag == one_argument_flag:
                    if self.accepted_arguments[flag] != None:
                        value = self.accepted_arguments[flag]
                    else:
                        value = self.parser.return_default_value()
        return value


def run_program_to_return_value_of_specific_flag():
    arguments_list = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyProgram(arguments_list)
    specific_flag = "-d"
    print("The value of the flag", specific_flag, "is", obj.return_value_of_a_specific_flag(specific_flag))


def run_program_to_return_default_value_when_flag_missing_it():
    arguments_list = {"-l": False, "-p": None, "-d": "/usr/logs"}
    obj = MyProgram(arguments_list)
    specific_flag = "-p"
    print("The default value of the flag", specific_flag, "is", obj.return_value_of_a_specific_flag(specific_flag))


def run_program_when_arguments_do_not_match_schema():
    arguments_list = {"-MMM": False, "-p": 8080, "-d": "/usr/logs"}
    MyProgram(arguments_list)


def run_program_when_value_is_a_negative_integer():
    arguments_list = {"-l": False, "-p": -8, "-d": "/usr/logs"}
    MyProgram(arguments_list)


if __name__ == "__main__":
    run_program_to_return_value_of_specific_flag()
    run_program_to_return_default_value_when_flag_missing_it()
    run_program_when_arguments_do_not_match_schema()
    run_program_when_value_is_a_negative_integer()
