from birthday_greetings.birthday_greetings import SendBirthdayNote, INPUT_FILE

obj = SendBirthdayNote()


def test_read_input_file():
    print(obj.read_input_file(INPUT_FILE))


def test_send_birthday_note():
    list_of_friends = obj.read_input_file(INPUT_FILE)
    print(obj.determine_birthday_note(list_of_friends, "1982/10/08"))
    print(obj.determine_birthday_note(list_of_friends, "1975/09/11"))


def test_generate_email():
    friend = ['Doe', 'John', '1982/10/08', 'john.doe@foobar.com']
    print(obj.generate_email(friend))
