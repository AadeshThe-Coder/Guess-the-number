import random

TRIES = {"easy": 10, "hard": 5}

def guess_number():
    level = input("Choose a difficulty (easy or hard): ").strip().lower()
    while level not in TRIES:
        level = input("Please type easy or hard: ").strip().lower()

    secret = random.randint(1, 100)
    attempts_left = TRIES[level]
    print(f"I'm thinking of a number from 1 to 100. You have {attempts_left} tries.")

    while attempts_left > 0:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if guess == secret:
            print("You won!")
            return
        attempts_left -= 1
        print("Too low." if guess < secret else "Too high.", f"{attempts_left} tries left.")
    print(f"You lost. The number was {secret}.")

if __name__ == "__main__":
    guess_number()
