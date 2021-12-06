from args.code.parser import MyParser


class MyProgram:
    def __init__(self, arguments):
        self.accepted_arguments = {}
        self.accepted_arguments = arguments
        self.schema = ["-l", "-p", "-d"]
        self.parser = MyParser(self.schema, self.accepted_arguments)

    def return_value_of_a_specific_flag(self, one_argument_flag):
        if self.parser.list_matches_schema:
            for flag in self.parser.arguments.keys():
                if flag == one_argument_flag:
                    print("The value of the flag", flag, "is", self.accepted_arguments[flag])
                    return self.accepted_arguments[flag]


def run_program():
    arguments_list = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyProgram(arguments_list)
    specific_flag = "-d"
    obj.return_value_of_a_specific_flag(specific_flag)


if __name__ == "__main__":
    run_program()
