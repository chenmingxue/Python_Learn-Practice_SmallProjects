#Write a Python class which has two methods get_String and print_String.
#get_String accept a string from the user and print_String print the string in upper case.

class ToUpperCase:
  def __init__(self, input_string="hello world"):
    self.input_string = inputString

  def get_String(self, inputString):
    self.input_string = inputString

  def print_String(self):
    return self.input_string.upper()


if __name__ == "__main__":
  inputString = input("Please key in your string: ")
  toUpperString = ToUpperCase()
  string_to_change = toUpperString.get_String(inputString)
  print(to_UpperString.print_String())
