#To guess a number that computer generated.
#1. Give a range of the number (0~input) and computer will generate a random number in the range
#2. Give a number of guess time that you can find it
#3. Key in the guess number and computer will tell if it is too big, too small, or correct
#4. Computer will count how many times you guess and compare to the guess time.
import random

class GuessNumber:
    def __init__(self, given_range=100):
        self.result = random.randint(1, given_range)

    def guess(self, input_number = 0):
        if input_number == self.result:
            return "Correct"
        elif input_number > self.result:
            return "Too big"
        else:
            return "Too small"

if __name__ == "__main__":
    while True:
        try:
            given_range = int(input("please enter a number larger than 0 (for example 100), and computer will make a random number: "))
            if given_range <= 0:
                print("Please key in a number > 0")
                continue
            break
        except:
            print("Please key in a valid number")
    guessnumber = GuessNumber(given_range)
    answer = guessnumber.guess()
    m = int(input("Please key in no more than how many times (smartness) you believe you can make it: "))
    n = 0
    while answer != "Correct":
        n += 1
        input_number = int(input("please put your guess < %d: " %given_range))
        answer = guessnumber.guess(input_number)
        print(answer)
    if n <= m:
        print("Great job, you are smart!")
    else:
        print("Good, you need to play more")
