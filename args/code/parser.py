class MyParser:
    def __init__(self, schema, arguments):
        self.schema = schema
        self.arguments = {}
        self.arguments = arguments

    def verify_list_of_arguments_matches_the_schema(self):
        schema = self.schema
        arguments = self.arguments
        arguments_value = False
        # verify list of arguments matches the schema
        for flag in schema:
            if flag not in arguments.keys():
                print("List of arguments does not have", flag, "flag")
                return arguments_value
            else:
                arguments_value = True
                return arguments_value
