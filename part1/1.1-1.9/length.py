text = input("Please input a string: ")
length = len(text)
if length < 5:
  print("'{}' has less than 5 characters.".format(text))
elif length > 5:
  print("'{}' has more than 5 characters.".format(text))
else:
  print("'{}' has exactly 5 characters.".format(text))
