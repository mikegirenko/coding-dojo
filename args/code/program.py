from args.code.parser import MyParser

class MyProgram:
    def __init__(self, list_of_args):
        self.accepted_list = {}
        self.accepted_list = list_of_args

    def accept_list_of_args(self):
        return self.accepted_list

    def make_schema(self):
        schema = []
        for key in self.accepted_list.keys():
            schema.append(key)
        return schema

    def pass_arguments_to_parser(self): # TODO continue here
        schema = self.make_schema()
        obj = MyParser(schema, self.accepted_list)
        obj.verify_arguments()


    def return_one_flag_value(self, one_argument_flag):
        for flag in self.accepted_list.keys():
            if flag == one_argument_flag:
                return self.accepted_list[flag]
