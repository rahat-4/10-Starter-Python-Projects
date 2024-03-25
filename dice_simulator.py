from random import randint


def roll_dice(amount: int) -> list[int]:
    """
    Rolls some dice and returns the results as a list
    :param amount: The amount of dice to roll
    returns: A list of dice rolls
    """
    if amount <= 0:
        raise ValueError

    rolls: list[int] = [randint(1, 6) for _ in range(amount)]

    return rolls


def main():
    while True:
        try:
            user_input: str = input("How many dice would you ike to roll? ")

            # To exit the game
            if user_input.lower() == "exit":
                print("Thanks for playing.")
                break

            # Try to parse the user_input to int
            print(*roll_dice(int(user_input)), sep=", ")

        except ValueError:
            print(
                "(Please enter a valid number or if you want to stop this game please enter 'exit')"
            )
            continue


if __name__ == "__main__":
    main()
