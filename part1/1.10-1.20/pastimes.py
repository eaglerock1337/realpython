import csv
import os

my_path = "/home/eaglerock/realpython/part1/1.10-1.20/practice_files/"

readcsv = os.path.join(my_path, "pastimes.csv")
writecsv = os.path.join(my_path, "categorized pastimes.csv")

# Kill file to write before attempting to make a fresh one
if os.path.exists(writecsv):
  os.remove(writecsv)

# Opening both files for reading and writing, respectfully
with open(readcsv, "r") as my_input_file, \
     open(writecsv, "w") as my_output_file:

  # CSV Reader and Writer setup
  pastimes = csv.reader(my_input_file)
  categorized = csv.writer(my_output_file)

  # Skip the read header and write header of output csv
  next(pastimes)
  categorized.writerow(["Name", "Favorite Pastime", "Type of Pastime"])

  print("Pastimes found:")

  # Go through the rows in input csv
  for row in pastimes:
    # Print the list to the screen
    print(row)
    # Categorize the pastime if the word "fighting" is found
    if row[1].lower().find("fighting") != -1:
      row.append("Combat")
    else:
      row.append("Other")

    # Write the populated row to the new csv file
    categorized.writerow(row)

with open(writecsv, "r") as my_check_file:
  checkcsv = csv.reader(my_check_file)
  next(checkcsv)
  print("\n New Pastimes:")
  for row in checkcsv:
    print(row)
