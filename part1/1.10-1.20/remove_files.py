import os

my_path = "/home/eaglerock/python/course/part1/1.10-1.20/practice_files/little pics"

for folder, subfolders, names in os.walk(my_path):
  for name in names:
    if name.lower().endswith(".jpg") and os.path.getsize(os.path.join(folder, name)) < 2000:
      print("Deleting {}...".format(os.path.join(folder, name)))
      os.remove(os.path.join(folder, name))
