#  Aims:
#  Create a program that asks the user to enter their name and their age.
#  Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
#  Extras:
#
#  Add on to the previous program by asking the user for another number and
#  printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#  Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

import datetime
while True:
  try:
    name = input("What is your name? ")
    if not name.isalpha():
      raise ValueError
    age = int(input("What is your age? "))
    if age < 0:
      raise ValueError
    result = str(datetime.date.today().year + 100 - age)
#Extra work
    multiply = int(input("How many times you want to copy the following conversation?\n(Enter 1 to skip) "))
    msg = "Your 100th birthday would be celebrated on " + result + "if you are " + str(age) + " by now, " + name + ".\n"
    print((msg)*multiply)
    break
  except ValueError:
    print("Please type your information properly!")
