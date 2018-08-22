mypoem = open("poem.txt", "r")

for line in mypoem.readlines():
 print(line, end="")

mypoem.close()

with open("poem.txt", "r") as withpoem:
  for line in withpoem.readlines():
    print(line, end="") 

infile = open("poem.txt", "r")
outfile = open("poem2.txt", "w")

outfile.writelines(infile.readlines())

infile.close()
outfile.close()

with open("poem.txt", "r") as within, open("output.txt", "w") as without:
  without.writelines(within.readlines())

append = open("output.txt", "a")

append.writelines("This is my extra line. Whee.\n")

append.close()
