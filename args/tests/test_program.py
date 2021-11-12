import pytest

from args.code.program import MyProgram


def test_it():
    list_1 = [1,2]
    obj = MyProgram(list_1)
    assert obj.accept_list_of_args() == list_1
