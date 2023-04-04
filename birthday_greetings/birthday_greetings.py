INPUT_FILE = "list_of_friends"

class SendBirthdayNote:

    def read_input_file(self, file_name):
        with open(file_name) as file_object:
            lines = file_object.readlines()

        return lines

    def send_birthday_note(self):
        pass


if __name__ == "__main__":
    obj = SendBirthdayNote()
