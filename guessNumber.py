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
            given_range = int(input("please enter a number >0, for example 100: "))
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
        print("You are smart!")
    else:
        print("You need to play more, you are not as smart as you think")
