class ReverseSentence:
  def __init__(self, sentence="Hello World"):
    self.sentence = sentence

  def reverse(self):
    return " ".join(self.sentence.split(" ")[::-1])


if __name__ == "__main__":
  sentence = input("Please write your sentence: ")
  reverse_sentence = ReverseSentence(sentence)
  print("The reversed sentence is: ", reverse_sentence.reverse())
