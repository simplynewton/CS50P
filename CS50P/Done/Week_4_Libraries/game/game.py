import random

def positive_integer(prompt):
    while True:
        try:
            integer = int(input(prompt))

            if integer> 0:
                return integer #holy brain rot my brain is cooked

        except ValueError:
            pass

def guessdanumber(level):
    secretnumber = random.randint(1, level)

    while True:
        guess = positive_integer("Guess: ")
        if guess < secretnumber:
            print("Too small!")
        elif guess> secretnumber:
            print("Too large!")
        else:
            print("Just right!")
            break

def main():
    level = positive_integer("Level: ")
    guessdanumber(level)
if __name__ == "__main__":
    main()
