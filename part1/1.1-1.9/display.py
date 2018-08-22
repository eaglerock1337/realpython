weight = 0.2
animal = "newt"
print("The weight of a", animal, "is", str(weight), "pounds.")
print("The weight of a {} is {} pounds.".format(animal, weight))
print("The weight of a {1} is {0} pounds.".format(weight, animal))
print("The weight of a {aml} is {wgt} pounds.".format(wgt=0.2, aml="newt"))
# This would work if I was running Python 3.6.
#print(f"The weight of a {animal} is {weight} pounds.")
