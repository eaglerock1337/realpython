class Dog(object):

  # Class Attribute
  species = 'mammal'

  # Initializer / Instance Attributes
  def __init__(self, name, age):
    self.name = name
    self.age = age


# Create three dogs
scooby = Dog("Scooby-doo", 49)
pluto = Dog("Pluto", 88)
odie = Dog("Odie", 40)


def get_biggest_number(*ages):
  return max(ages)

print("The oldest dog is {} years old.".format(get_biggest_number(scooby.age, pluto.age, odie.age)))
