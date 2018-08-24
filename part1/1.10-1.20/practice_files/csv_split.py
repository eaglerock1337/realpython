import csv
import argparse
import os

"""
csv_split.py
8/23/2018 Peter P. Marks

Write a script that will take three required command line arguments - input_file ,
output_file , and the row_limit . From those arguments, split the input CSV into
multiple files based on the row_limit argument.

Arguments:
  1. -i : input file name
  2. -o : output file name
  3. -r : row limit to split

Default settings:
  1. output_path is the current directory
  2. headers are displayed on each split file
  3. the default delimiter is a comma

Example usage:
# split csv by every 100 rows
>> python csv_split.py -i input.csv -o output -r 100
"""

def get_args()
  # Retrieves the three arguments that should be given
  parser = argparse.ArgumentParser(prog='csv_split', description="split a csv file into multiple files")
  parser.add_argument("-i", "--input", required=True, type=str, help="The input csv file")
  parser.add_argument("-o", "--output", required=True, type=str, help="The output csv file(s) to be used (without the extension)")
  parser.add_argument("-r", "--rows", required=True, type=int, help="How many rows each split .csv should have")

  return parser.parse_args()

def validate_input(input_file)
  return os.path.exists(input_file)
#  if os.path.exists(input_file) == False:
#    return False
#  else:
#    return True

def validate_csv(input_file, row_limit)
  with open(input_file, "r") as my_csv_file
    my_csv = csv.reader(my_csv_file)
    next(my_csv)
    rows = 0
    for row in my_csv:
      row += 1
  return rows > row_limit

def validate_output(output_file)
  if outputfile.endswith(".csv"):
    print("WARNING: output_file ends with .csv. Truncating.")
    return output_file[0:len(output_file) - 4]
  else:
    return output_file

#
# Main Function
#

# Retrieving arguments from command-line
my_args = get_args()

# Validating input file exists
validate_input(my_args.input) or die("ERROR: Input file not found.")

# Validating input file is a valid csv with
validate_csv(my_args.input) or die("ERROR: Input .csv file not valid for number of rows.")

# Validate output csv name doesn't end with .csv
validated_output = validate_output(my_args.output)

