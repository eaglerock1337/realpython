my_output_file = open("hello.txt", "w")

my_output_file.writelines("This is the first line of this file.")

my_output_file.close()

my_output_file2 = open("hello.txt", "w")

lines_to_write = ["This is my file.\n", "There are many like it,\n", "but this one is mine.\n"]

my_output_file2.writelines(lines_to_write)

my_output_file2.close()

my_output_file3 = open("hello.txt", "a")

my_output_file3.writelines("NON SEQUITUR\n")

my_output_file3.close()

my_input_file = open("hello.txt", "r")

print(my_input_file.readlines())

my_input_file.close()

my_input_file2 = open("hello.txt", "r")

for line in my_input_file2.readlines():
  print(line, end="")

my_input_file2.close()

my_input_file3 = open("hello.txt", "r")

line = my_input_file3.readline()
while line != "":
  print(line, end="")
  line = my_input_file3.readline()

my_input_file3.close()
