#!/usr/bin/python3
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

def get_args():
  # Retrieves the three arguments that should be given
  parser = argparse.ArgumentParser(prog='csv_split', description="split a csv file into multiple files")
  parser.add_argument("-i", "--input", required=True, type=str, help="The input csv file")
  parser.add_argument("-o", "--output", required=True, type=str, help="The output csv file(s) to be used (without the extension)")
  parser.add_argument("-r", "--rows", required=True, type=int, help="How many rows each split .csv should have")

  return parser.parse_args()

def validate_input(input_file):
  return os.path.exists(input_file)

def validate_csv(input_file, row_limit):
  with open(input_file, "r") as my_csv_file:
    my_csv = csv.reader(my_csv_file)
    next(my_csv)
    rows = 0
    for row in my_csv:
      rows += 1
  return rows > row_limit

def validate_output(output_file):
  if output_file.endswith(".csv"):
    print("WARNING: Output filename ends with .csv. Truncating.")
    return output_file[0:len(output_file) - 4]
  else:
    return output_file

def write_csv(output_csv, iteration, name):
  filename = "{}{:03}.csv".format(name, iteration)
  print("Chunk {}: Writing {} rows to {}...".format(iteration, len(output_csv) - 1, filename))

  with open(filename, "w") as my_output_file:
    my_output_csv = csv.writer(my_output_file)
    my_output_csv.writerows(output_csv)

def split_csv(input_csv, row_limit, output):
  print("Splitting {} after every {} rows...".format(input_csv, row_limit))

  with open(input_csv, "r") as my_input_file:
    my_input_csv = csv.reader(my_input_file)
    my_header = next(my_input_csv)
    
    csv_file = []
    csv_file.append(my_header)

    curr_csv = 0
    curr_row = 0
    for row in my_input_csv:
      csv_file.append(row)
      curr_row += 1
      if curr_row >= row_limit:
        write_csv(csv_file, curr_csv, output)
        del(csv_file)
        csv_file = []
        csv_file.append(my_header)
        curr_csv += 1
        curr_row = 0
#
# Main Function
#

# Retrieving arguments from command-line
my_args = get_args()

# Validating input file exists
validate_input(my_args.input) or die("ERROR: Input file not found.")

# Validating input file is a valid csv with enough rows
validate_csv(my_args.input, my_args.rows) or die("ERROR: Input .csv file not valid for number of rows.")

# Validate output csv name doesn't end with .csv
good_output = validate_output(my_args.output)

# Split input csv data into a list of lists based on specified rows
csv_files = split_csv(my_args.input, my_args.rows, good_output)


