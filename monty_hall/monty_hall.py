from random import randrange

OPTIONS = ["Just choose door", "Prize", "Goat"]


def display_doors(doors):
    print("\n")
    print("-----")
    print(doors)
    print("-----")


def choose_option(options):
    i = randrange(len(options))

    return options[i]


def monty_hall_game():
    doors = ["?", "?", "?"]
    counter = 1
    while counter <= 3:
        display_doors(doors)
        user_input = input("Choose door: ")
        selected_option = choose_option(OPTIONS)
        if selected_option == OPTIONS[0]:
            counter -= 1
        if selected_option == OPTIONS[1]:
            print("You are a winner!")
            return
        doors[int(user_input)] = selected_option
        counter += 1
        display_doors(doors)


if __name__ == "__main__":
    monty_hall_game()
