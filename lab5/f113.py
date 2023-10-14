import random

def guess_the_number():

    secret_number = random.randint(1, 20)
    guesses = 0


    player_name = input("Hello! What is your name?\n")
    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Take a guess.\n"))
            guesses += 1

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {player_name}! You guessed my number in {guesses} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
