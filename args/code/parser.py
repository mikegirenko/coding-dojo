"""
parser
        a) accept schema specifying number of flags, types, and accepted values
        b) verify list of arguments matches the schema
        c) specify

"""


class MyParser:
    def __init__(self, schema, arguments):
        self.schema = []
        self.schema = schema
        self.arguments = {}
        self.arguments = arguments

    def return_accepted_schema(self):
        return self.schema

    def verify_arguments(self):
        schema = self.return_accepted_schema()
        arguments = self.arguments
        # verify list of arguments matches the schema
        for flag in schema:
            if flag not in arguments.keys():
                print("List of arguments does not have" , flag, "flag")