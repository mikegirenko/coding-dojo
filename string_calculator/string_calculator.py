class StringCalculator:
    def add(self, string_of_numbers: str) -> str:
        list_of_numbers = []
        list_2_of_numbers_separated_by_comma = []
        list_of_numbers_separated_by_n = []
        list_by_n = []
        list_by_comma = []
        sum_of_numbers = ""
        if string_of_numbers == "":
            sum_of_numbers = "0"
        else:
            if "\n" in string_of_numbers:
                list_separated_by_comma = string_of_numbers.split(",")
                for item in list_separated_by_comma:
                    if "\n" in item:
                        list_of_numbers_separated_by_n = item.split("\n")
                    else:
                        list_2_of_numbers_separated_by_comma.append(item)
                for item in list_of_numbers_separated_by_n:
                    list_by_n.append(int(item))
                for item in list_2_of_numbers_separated_by_comma:
                    list_by_comma.append(int(item))
                sum_of_numbers = sum(list_by_n) + sum(list_by_comma)
            if "\n" not in string_of_numbers:
                list_of_strings = string_of_numbers.split(",")
                for item in list_of_strings:
                    list_of_numbers.append(int(item))

                sum_of_numbers = sum(list_of_numbers)

        return sum_of_numbers


if __name__ == "__main__":
    obj = StringCalculator()
    print(obj.add("1, 2, 3"))
