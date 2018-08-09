def printnumbers(list):
  for i in list:
    if i >= 1 and i <= 20:
      print(i)

mylist = [2, 4, 8, 16, 32, 64]
hurleyslist = [4, 8, 15, 16, 23, 42]

print("My list:")
printnumbers(mylist)
print("Hurley's list:")
printnumbers(hurleyslist)
