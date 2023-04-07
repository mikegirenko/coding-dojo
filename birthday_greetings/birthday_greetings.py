INPUT_FILE = "list_of_friends"


class SendBirthdayNote:
    def read_input_file(self, file_name) -> list:
        final_list_of_friends = []
        with open(file_name) as file_object:
            lines = file_object.read()
            list_of_friends = lines.split("\n")
        for friend in list_of_friends[
            1:
        ]:  # removing last_name, first_name, date_of_birth, email
            clean_friend = friend.replace(" ", "")
            final_list_of_friends.append(clean_friend)

        return final_list_of_friends

    def born_february_twenty_nine(self, friend):
        born_february_twenty_nine = False
        split_friend = friend.split(",")
        date = split_friend[2]
        stripped_date = date.strip()
        date_len = len(stripped_date)
        if date_len == 12:
            if stripped_date[6:11] == "02/29":
                born_february_twenty_nine = True
        if date_len == 10:
            if stripped_date[5:10] == "02/29":
                born_february_twenty_nine = True
        return born_february_twenty_nine

    def determine_birthday_friend(self, list_of_friends, current_date) -> list:
        these_friends_get_an_email = []
        for friend in list_of_friends:
            split_friend = friend.split(",")
            if self.born_february_twenty_nine(str(split_friend)):
                if current_date[5:10] == "02/28":
                    these_friends_get_an_email = split_friend
            if split_friend[2] == current_date:
                these_friends_get_an_email.append(split_friend)

        return these_friends_get_an_email

    def generate_note(self, friend) -> tuple:
        subject = "Subject: Happy birthday!"
        friend_first_name = friend[1]
        body = f"Happy birthday, dear {friend_first_name}!"

        return subject, body

    def generate_note_for_someone_else(
        self, list_of_friends, current_date, reminder_recipient
    ):
        birthday_friend = self.determine_birthday_friend(list_of_friends, current_date)
        subject = "Subject: Birthday Reminder"
        body = (
            f"Dear {reminder_recipient}, Today is {birthday_friend[0][1]} {birthday_friend[0][0]}'s birthday. "
            f"Don't forget to send him a message!"
        )

        return subject, body

    def generate_single_note(self, list_of_friends, current_date, reminder_recipient):
        birthday_friends = self.determine_birthday_friend(list_of_friends, current_date)
        full_name_1 = f"{birthday_friends[0][1]} {birthday_friends[0][0]}"
        full_name_2 = f"{birthday_friends[1][1]} {birthday_friends[1][0]}"
        subject = "Subject: Birthday Reminder"
        body = f"Dear {reminder_recipient}, Today is {full_name_1} and {full_name_2}'s birthday. " \
               f"Don't forget to send them a message!"

        return subject, body


if __name__ == "__main__":
    obj = SendBirthdayNote()
    list_of_friends = obj.read_input_file(INPUT_FILE)

    current_date = "1982/10/08"
    birthday_friend = obj.determine_birthday_friend(list_of_friends, current_date)
    subject, body = obj.generate_note(birthday_friend[0])
    print("Current date is", current_date)
    print(subject, "\n", body)

    current_date = "1992/02/28"
    birthday_friend = obj.determine_birthday_friend(list_of_friends, current_date)
    subject, body = obj.generate_note(birthday_friend)
    print("Current date is", current_date)
    print(subject, "\n", body)

    current_date = "1982/10/08"
    reminder_recipient = "Mary"
    subject, body = obj.generate_note_for_someone_else(
        list_of_friends, current_date, reminder_recipient
    )
    print("Current date is", current_date)
    print(subject, "\n", body)


    current_date = "1982/10/08"
    reminder_recipient = "Mary"
    subject, body = obj.generate_single_note(
        list_of_friends, current_date, reminder_recipient
    )
    print("Current date is", current_date)
    print(subject, "\n", body)
