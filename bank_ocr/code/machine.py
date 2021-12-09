
class Machine:
    def __init__(self, letter):
        self.letter = letter
        self.output_file = []

    def validate_letter_and_populate_file(self):
        raw_input = self.letter
        for character in raw_input:
            if isinstance(character, int):
                self.output_file.append(character)
        print(self.output_file)
        return self.output_file

    def accept_letter_and_produce_file(self):
        print("File populated with", self.validate_letter_and_populate_file())
