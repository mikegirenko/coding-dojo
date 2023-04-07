from code_cracker.code_cracker import *

obj = CodeCracker()


def test_message_decryptor():
    message = '!)"'
    assert obj.decrypt_message(message) == "abc"


def test_empty_string():
    message = ''
    assert obj.decrypt_message(message) == ""


def test_integer():
    message = "wxyz"
    assert obj.enrypt_message(message) == "lmno"
