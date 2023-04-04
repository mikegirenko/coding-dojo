INPUT_FILE = "list_of_friends"

class SendBirthdayNote:

    def read_input_file(self, file_name) -> list:
        final_list_of_friends = []
        with open(file_name) as file_object:
            lines = file_object.read()
            list_of_friends = lines.split("\n")
        for friend in list_of_friends[1:]: # removing  last_name, first_name, date_of_birth, email
            clean_friend = friend.replace(" ", "")
            final_list_of_friends.append(clean_friend)

        return final_list_of_friends

    def born_february_twenty_nine(self, friend):
        born_february_twenty_nine = False
        split_friend = friend.split(",")
        date = split_friend[2]
        if date[5:] == "02/29":
            born_february_twenty_nine = True

        return born_february_twenty_nine



    def determine_birthday_friend(self, list_of_friends, current_date):
        this_friend_gets_an_email = ""
        for friend in list_of_friends:
            split_friend = friend.split(",")
            if self.born_february_twenty_nine(str(split_friend)):
                if current_date[5] == "02/28":
                    print("yes")
            if split_friend[2] == current_date:
                this_friend_gets_an_email = split_friend

        return this_friend_gets_an_email

    def generate_email(self, friend) -> tuple:
        subject = "Subject: Happy birthday!"
        body = f"Happy birthday, dear {friend[1]}!"

        return subject, body


if __name__ == "__main__":
    obj = SendBirthdayNote()
    list_of_friends = obj.read_input_file(INPUT_FILE)
    current_date = "1982/10/08"
    birthday_friend = obj.determine_birthday_friend(list_of_friends, current_date)
    subject, body = obj.generate_email(birthday_friend)
    print(subject, "\n", body)
