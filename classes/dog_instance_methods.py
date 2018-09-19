class Dog(object):

  # Class Attribute
  species = 'mammal'

  # Initializer / Instance Attributes
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # instance method
  def description(self):
    return "{} is {} years old".format(self.name, self.age)

  # instance method
  def speak(self, sound):
    return "{} says {}".format(self.name, sound)


# Need a dog
odie = Dog("Odie", 40)

# Print stuffs
print(odie.description())
print(odie.speak("Arf!"))
