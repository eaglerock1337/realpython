def cel(fah):
  return (fah - 32) * 5/9

def fah(cel):
  return cel * 9/5 + 32

fah1 = 72
cel1 = cel(fah1)
cel2 = 37
fah2 = fah(cel2)

print("{} degrees Fahrenheit = {} degrees Celsius.".format(fah1, cel1))
print("{} degrees Celsius = {} degrees Fahrenheit.".format(cel2, fah2))

