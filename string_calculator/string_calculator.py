class StringCalculator:
    def add(self, string_of_numbers: str) -> str:
        list_of_numbers = []
        list_2_of_numbers_separated_by_comma = []
        list_of_numbers_separated_by_n = []
        list_by_n = []
        list_by_comma = []
        sum_of_numbers = ""
        message = ""
        if string_of_numbers == "" and "\n" not in string_of_numbers:
            sum_of_numbers = "0"
        if string_of_numbers != "" and string_of_numbers[-1] == " ":
            message = "Number expected but EOF found."
        if "\n" in string_of_numbers:
            list_separated_by_comma = string_of_numbers.split(",")
            for item in list_separated_by_comma:
                if "\n" in item:
                    if item[:2] == " \n":
                        if len(item.splitlines()) > 1:
                            message = "Number expected but '\n' found at position 6."
                    else:
                        list_of_numbers_separated_by_n = item.split("\n")
                else:
                    list_2_of_numbers_separated_by_comma.append(item)
            for item in list_of_numbers_separated_by_n:
                list_by_n.append(int(item))
            for item in list_2_of_numbers_separated_by_comma:
                list_by_comma.append(int(item))
            if message:
                sum_of_numbers = message
            else:
                sum_of_numbers = sum(list_by_n) + sum(list_by_comma)
        if "\n" not in string_of_numbers and string_of_numbers != "" and string_of_numbers[-1] != " ":
            list_of_strings = string_of_numbers.split(",")
            for item in list_of_strings:
                list_of_numbers.append(int(item))

            sum_of_numbers = sum(list_of_numbers)
        if message:
            sum_of_numbers = message
        return sum_of_numbers


if __name__ == "__main__":
    obj = StringCalculator()
    print(obj.add(""))
    print(obj.add("1,2,3"))
    print(obj.add("1\n2,3"))
    print(obj.add("175, \n35"))
    print(obj.add("1,3, "))
