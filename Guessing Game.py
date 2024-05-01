import random

def generate_Random_number():
    digits = random.sample(range(10), 3)
    return digits

def compare_numbers(random_num, guess):
    clues = []
    for i in range(3):
        if guess[i] == random_num[i]:
            clues.append("Match")
        elif guess[i] in random_num:
            clues.append("Close")
        else:
            clues.append("Nope")
    return clues

def game():
    random_num = generate_Random_number()
    print("Welcome to the Number Guessing Game!")

    while True:
        guess = int(input("Enter your guess (3 non-repeating digits): "))
        guess_list = [int(digit) for digit in str(guess)]

        if len(guess_list) != 3 or len(set(guess_list)) != 3:
            print("Please enter a valid 3-digit number with non-repeating digits.")
            continue

        result_clues = compare_numbers(random_num, guess_list)
        print("Clues:", result_clues)

        if result_clues == ["Match", "Match", "Match"]:
            print("Congratulations! You got it.")
            break


game()
