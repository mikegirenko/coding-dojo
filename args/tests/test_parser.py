from args.code.parser import MyParser

def test_parser_accepts_schema():
    schema = ["-l", "-p", "-d"]
    args = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyParser(schema, args)

    assert obj.return_accepted_schema


def test_parser_returns_true_if_arguments_match_schema():
    schema = ["-l", "-p", "-d"]
    args = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyParser(schema, args)
    assert obj.verify_arguments()


def test_parser_returns_false_if_arguments_do_not_match_schema():
    schema = ["-l", "-p", "-d"]
    args = {"-W": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyParser(schema, args)
    assert not obj.verify_arguments()