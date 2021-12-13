
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

    def populate_number_one(self):
        print(" ")
        print("| ")
        print("| ", end=" ")

    def populate_number_two(self):
        print("_")
        print("_|")
        print("|_")

    def print_account_number(self):
        self.populate_number_one()
        self.populate_number_two()

    def accept_letter_and_produce_file(self):
        print("File populated with", self.populate_account_numbers())
