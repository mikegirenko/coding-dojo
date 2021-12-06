from args.code.parser import MyParser


def test_parser_accepts_schema():
    schema = ["-l", "-p", "-d"]
    args = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyParser(schema, args)

    assert obj.schema == schema


def test_parser_returns_true_if_arguments_match_schema():
    schema = ["-l", "-p", "-d"]
    args = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyParser(schema, args)

    assert obj.verify_list_of_arguments_matches_the_schema()


def test_parser_returns_false_if_arguments_do_not_match_schema():
    schema = ["-l", "-p", "-d"]
    args = {"-W": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyParser(schema, args)

    assert not obj.verify_list_of_arguments_matches_the_schema()


def test_default_value_returned_when_flag_missing_it():
    schema = ["-l", "-p", "-d"]
    args = {"-l": None, "-p": 8080, "-d": "/usr/logs"}
    default_values = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyParser(schema, args)

    assert obj.return_default_value() == default_values["-l"]


def test_default_value_not_returned_when_flag_not_missing_it():
    schema = ["-l", "-p", "-d"]
    args = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    obj = MyParser(schema, args)

    assert not obj.return_default_value()
