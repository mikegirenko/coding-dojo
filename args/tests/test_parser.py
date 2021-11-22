from args.code.parser import MyParser

def test_parser_accepts_schema():
    schema = ["-l", "-p", "-d"]
    args = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyParser(schema, args)

    assert obj.return_accepted_schema


def test_parser_verifies_arguments():
    schema = ["-l", "-p", "-d"]
    args = {"-b": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyParser(schema, args)
    obj.verify_arguments()

