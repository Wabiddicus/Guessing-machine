import random

random_number = random.randint(1, 25)
chances_left = 3

while chances_left > 0:
    guess = int(input("Enter your guess (1-25):"))
    if guess == random_number:
        print("Congratz! you guessed the number!")
        break
    else:
        chances_left -= 1
        if chances_left == 0:
            print("no more chances left. The number was:", random_number)
        else:
            print("sorry, that's not correct, you have", chances_left, "chances left.")
