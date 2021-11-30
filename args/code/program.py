class MyProgram:
    def __init__(self, list_of_args):
        self.this_list = {}
        self.this_list = list_of_args

    def accept_list_of_args(self):
        return self.this_list

    def return_one_flag_value(self, one_argument_flag):
        for flag in self.this_list.keys():
            if flag == one_argument_flag:
                return self.this_list[flag]
