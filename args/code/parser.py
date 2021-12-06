class MyParser:
    def __init__(self, schema, arguments):
        self.schema = schema
        self.arguments = {}
        self.arguments = arguments
        self.list_matches_schema = self.verify_list_of_arguments_matches_the_schema()

    def verify_list_of_arguments_matches_the_schema(self):
        schema = self.schema
        arguments = self.arguments
        arguments_value = False
        for flag in schema:
            if flag not in arguments.keys():
                print("List of arguments does not have", flag, "flag")
                return arguments_value
            else:
                arguments_value = True
                return arguments_value

    def return_default_value(self):
        default_values = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
        schema = self.schema
        arguments = self.arguments

        for flag in schema:
            if arguments[flag] == None:
                return default_values[flag]
