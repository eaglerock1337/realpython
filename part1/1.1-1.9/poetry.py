from random import choice

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

def makePoem():
  noun1 = choice(nouns)
  nouns.remove(noun1)
  noun2 = choice(nouns)
  nouns.remove(noun2)
  noun3 = choice(nouns)
  verb1 = choice(verbs)
  verbs.remove(verb1)
  verb2 = choice(verbs)
  verbs.remove(verb2)
  verb3 = choice(verbs)
  adjective1 = choice(adjectives)
  adjectives.remove(adjective1)
  adjective2 = choice(adjectives)
  adjectives.remove(adjective2)
  adjective3 = choice(adjectives)
  adverb1 = choice(adverbs)
  preposition1 = choice(prepositions)
  prepositions.remove(preposition1)
  preposition2 = choice(prepositions)
  
  vowels = ["a", "e", "i", "o", "u"]
  if noun1[0].lower() in vowels:
    a_or_an = "An"
  else:
    a_or_an = "A"

  poem = "{} {} {}\n\n".format(a_or_an, adjective1, noun1)
  poem = poem + "{} {} {} {} {} the {} {}\n".format(a_or_an, adjective1, noun1, verb1, preposition1, adjective2, noun2)
  poem = poem + "{}, the {} {}\n".format(adverb1, noun1, verb2)
  poem += "the {} {} {} a {} {}".format(noun2, verb3, preposition2, adjective3, noun3)

  return poem

print(makePoem())
