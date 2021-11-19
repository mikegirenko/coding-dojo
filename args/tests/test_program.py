from args.code.program import MyProgram


def test_program_accepts_list_of_args():
    list_1 = [1,2]
    obj = MyProgram(list_1)
    assert obj.accept_list_of_args() == list_1


def test_program_accepts_schema():
    schema = {"-l": False, "-p": 8080, "-d": "/usr/logs"}
    print(schema)
