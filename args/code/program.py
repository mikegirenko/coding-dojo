from args.code.parser import MyParser


class MyProgram:
    def __init__(self, arguments):
        self.accepted_arguments = {}
        self.accepted_arguments = arguments
        self.schema = ["-l", "-p", "-d"]
        self.parser = MyParser(self.schema, self.accepted_arguments)

    def return_value_of_a_specific_flag(self, one_argument_flag):
        for flag in self.parser.arguments.keys():
            if flag == one_argument_flag:
                return self.accepted_arguments[flag]


def run_program():
    arguments_list = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyProgram(arguments_list)
    print("The value of the flag -d is", obj.return_value_of_a_specific_flag("-d"))


if __name__ == "__main__":
    run_program()
