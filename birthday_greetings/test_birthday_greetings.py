from birthday_greetings.birthday_greetings import *

obj = SendBirthdayNote()


def test_read_input_file():
    print(obj.read_input_file(INPUT_FILE))


def test_born_february_twenty_nine():
    friend_born_february_twenty_nine = "Smith,Stephen,1985/02/29,mary.smith@foobar.com"
    assert obj.born_february_twenty_nine(friend_born_february_twenty_nine)
    friend_not_born_february_twenty_nine = "Ann,Mary,1975/09/11,mary.ann@foobar.com"
    assert not obj.born_february_twenty_nine(friend_not_born_february_twenty_nine)


def test_send_birthday_note():
    list_of_friends = obj.read_input_file(INPUT_FILE)
    print(obj.determine_birthday_friend(list_of_friends, "1982/10/08"))
    print(obj.determine_birthday_friend(list_of_friends, "1975/09/11"))


def test_send_birthday_note_february_twenty_nine():
    list_of_friends = ["Smith,Stephen,1985/02/29,mary.smith@foobar.com"]
    print(obj.determine_birthday_friend(list_of_friends, "1975/02/28"))


def test_generate_note():
    friend = ["Doe", "John", "1982/10/08", "john.doe@foobar.com"]
    print(obj.generate_note(friend))


def test_generate_note_for_someone_else():
    list_of_friends = obj.read_input_file(INPUT_FILE)
    print(obj.generate_note_for_someone_else(list_of_friends, "1982/10/08", "Ann"))
