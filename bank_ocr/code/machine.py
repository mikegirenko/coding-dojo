class Machine:
    def __init__(self, letter):
        self.letter = letter

    def extract_account_numbers(self):
        raw_input = self.letter
        list_with_account_numbers = []
        for character in raw_input:
            if not isinstance(character, int):
                list_with_account_numbers.append("?")
            else:
                list_with_account_numbers.append(character)
        return list_with_account_numbers

    def populate_number_zero(self):
        return "* _ *\n*|_|*\n*|_|*"

    def populate_number_one(self):
        return "*  *\n* |*\n* |*"

    def populate_number_two(self):
        return "*_ *\n*_|*\n*|_*"

    def populate_number_three(self):
        return "*_ *\n*_|*\n*_|*"

    def populate_number_four(self):
        return "*  *\n*|_|*\n*  |*"

    def populate_number_five(self):
        return "* _*\n*|_*\n*_|*"

    def populate_number_six(self):
        return "* _*\n*|_*\n*|_|*"

    def populate_number_seven(self):
        return "* _*\n* |*\n* |*"

    def populate_number_eight(self):
        return "* _ *\n*|_|*\n*|_|*"

    def populate_number_nine(self):
        return "* _*\n*|_|*\n* _|*"

    def populate_file_with_real_account_numbers(self):
        account_numbers = self.extract_account_numbers()
        checksum_status = self.check_if_account_number_has_valid_checksum()
        output_file = open("output_file.txt", "a")
        for i in range(len(account_numbers)):
            if i == 0:
                output_file.write(self.populate_number_zero())
                output_file.write("\n")
            if i == 1:
                output_file.write(self.populate_number_one())
                output_file.write("\n")
            if i == 2:
                output_file.write(self.populate_number_two())
                output_file.write("\n")
            if i == 3:
                output_file.write(self.populate_number_three())
                output_file.write("\n")
            if i == 4:
                output_file.write(self.populate_number_four())
                output_file.write("\n")
            if i == 5:
                output_file.write(self.populate_number_five())
                output_file.write("\n")
            if i == 6:
                output_file.write(self.populate_number_six())
                output_file.write("\n")
            if i == 7:
                output_file.write(self.populate_number_seven())
                output_file.write("\n")
            if i == 8:
                output_file.write(self.populate_number_eight())
                output_file.write("\n")
            if i == 9:
                output_file.write(self.populate_number_nine())
                output_file.write("\n")
        if not checksum_status:
            if "?" not in account_numbers:
                output_file.write("ERR")
        if not checksum_status:
            if "?" in account_numbers:
                output_file.write("ILL")
        output_file.close()

    def accept_letter_and_produce_file(self):
        self.populate_file_with_real_account_numbers()
        print("File populated with", self.extract_account_numbers())

    def check_if_account_number_has_valid_checksum(self):
        account_numbers = self.extract_account_numbers()
        valid_checksum = False
        if "?" not in account_numbers:
            pair_1 = account_numbers[-1] + 2
            pair_2 = account_numbers[-2] + 3
            pair_3 = account_numbers[-3] + 4
            pair_4 = account_numbers[-4] + 5
            pair_5 = account_numbers[-5] + 6
            pair_6 = account_numbers[-6] + 7
            pair_7 = account_numbers[-7] + 8
            pair_8 = account_numbers[-8] + 9
            all_pairs = (
                pair_1 * pair_2 * pair_3 * pair_4 * pair_5 * pair_6 * pair_7 * pair_8
            )
            in_parenthesis = all_pairs * account_numbers[-9]
            if in_parenthesis % 11 == 0:
                valid_checksum = True
        return valid_checksum


if __name__ == "__main__":
    letter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    obj = Machine(letter)
    obj.accept_letter_and_produce_file()
