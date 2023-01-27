
class StringCalculator:

    def calculate_sum_of_numbers(self, string_of_numbers):
        list_of_numbers = []
        if string_of_numbers == "":
            sum_of_numbers = "0"
        else:
            list_of_strings = string_of_numbers.split(",")
            for item in list_of_strings:
                list_of_numbers.append(int(item))

            sum_of_numbers = sum(list_of_numbers)


        return sum_of_numbers


if __name__ == "__main__":
    obj = StringCalculator()
    print(obj.calculate_sum_of_numbers("1, 2, 3"))
