cats = []
for i in range(0,101):
  cats.append(0)

for rnd in range(1,101):
  for cat in range(1,101):
    if cat % rnd == 0:
      cats[cat] = not cats[cat]

print("The cats that have cats at the end are:")
for i in range(1, 101):
  if cats[i]:
    print("Cat {}".format(i))
    
