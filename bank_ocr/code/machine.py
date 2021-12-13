
class Machine:
    def __init__(self, letter):
        self.letter = letter

    def populate_account_numbers(self):
        raw_input = self.letter
        list_with_account_numbers = []
        for character in raw_input:
            if isinstance(character, int):
                list_with_account_numbers.append(character)
        return list_with_account_numbers

    def create_line_27_characters_long(self):
        return " " * 27

    def print_one_cell(self, character):
        print(character)

    def populate_number_zero(self):
        return ("* _ *\n*|_|*\n*|_|*")

    def populate_number_one(self):
        return("*  *\n* |*\n* |*")

    def populate_number_two(self):
        return ("*_ *\n*_|*\n*|_*")

    def populate_number_three(self):
        return ("*_ *\n*_|*\n*_|*")

    def print_account_number(self):
        output_file = open('output_file.txt', 'a')
        output_file.write(self.populate_number_zero())
        output_file.write("\nseparator\n")
        output_file.write(self.populate_number_one())
        output_file.write("\nseparator\n")
        output_file.writelines(self.populate_number_two())
        output_file.write("\nseparator\n")
        output_file.writelines(self.populate_number_three())
        output_file.write("\nseparator\n")
        output_file.close()

    def accept_letter_and_produce_file(self):
        print("File populated with", self.populate_account_numbers())
