class Roman:

    def number_below_eleven(self, normal_number):
        roman_number = ""
        if normal_number == 0:
            roman_number = "Romans did not have zero"
        if normal_number <= 3 and normal_number != 0:
            roman_number = "I" * normal_number
        if normal_number == 4:
            roman_number = "IV"
        if normal_number == 5:
            roman_number = "V"
        if 6 <= normal_number <= 8:
            roman_number = "V" + ("I" * (normal_number - 5))
        if normal_number == 9:
            roman_number = "IX"
        if normal_number == 10:
            roman_number = "X"

        return roman_number


    def number_below_fifty(self, normal_number):
        roman_number = ""
        if 10 < normal_number <= 13:
            roman_number = "X" + ("I" * (normal_number - 10))
        if normal_number == 14:
            roman_number = "XIV"
        if normal_number == 15:
            pass   # TODO continue here

        return roman_number

    def convert_from_normal_to_roman(self, normal_number):
        roman_number = ""
        if normal_number < 11:
            roman_number = self.number_below_eleven(normal_number)
        if 11 <= normal_number < 50:
            roman_number = self.number_below_fifty(normal_number)

        return roman_number


if __name__ == "__main__":
    obj = Roman()
    print("Roman numeral is", obj.convert_from_normal_to_roman(9))
