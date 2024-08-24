from random import randint
from math import log2, ceil
import pyinputplus as pyip


class GuessingGame:
    def __init__(self, min_num, max_num) -> None:
        self.min = min_num
        self.max = max_num
        self.max_attempts = ceil(log2(self.max - self.min))
        self.num = randint(min_num, max_num)
        self.attempts = 0
        print(f"You have {self.max_attempts - self.attempts} chance to try")

    def check_guess(self, guess):
        self.attempts += 1
        if guess > self.num:
            self.max = guess
            print(f"Please guess the smaller number between {self.min} and {self.max}.")
        elif guess < self.num:
            self.min = guess
            print(f"Please guess the bigger number between {self.min} and {self.max}.")
        else:
            print(f"You find it on {self.attempts} try!")
            return True

        print(f"You have {self.max_attempts - self.attempts} chance to try")


minimum = int(input('Please input minimum number: '))
maximum = int(input('Please input maximum number: '))
play = GuessingGame(minimum, maximum)
while True:
    user_input = pyip.inputInt(
        prompt=f"Enter an Integer between {play.min}-{play.max}: ", default=play.min, min=play.min, lessThan=play.max)
    finish = play.check_guess(user_input)

    if finish:
        menu_input = pyip.inputMenu(['Yes', 'No'],
                                    numbered=True,
                                    prompt='Do you like play again\n')
        if menu_input == 'Yes':
            minimum = int(input('Please input minimum number: '))
            maximum = int(input('Please input maximum number: '))
            play = GuessingGame(minimum, maximum)
            finish = False
        else:
            break
