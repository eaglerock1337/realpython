import os
import glob

my_path = "/home/eaglerock/python/course/part1/1.10-1.20/practice_files"

my_files = os.listdir(my_path)

print("Files in {}:".format(my_path))

for filename in my_files:
  print(os.path.join(my_path, filename))

my_images = os.path.join(my_path, "images")

my_png = os.path.join(my_images, "*.png")

print("\n.png files in {}:".format(my_images))

for filename in glob.glob(my_png):
  print(os.path.join(my_images, filename))

print("\nFiles to be renamed to end with .jpg:")

for folder, subfolders, names in os.walk(my_images):
  for name in names:
    filename, extension = os.path.splitext(name)
    if extension == ".png":
      print(os.path.join(folder, name))
      newname = filename + ".jpg"
      os.rename(os.path.join(folder, name), os.path.join(folder, newname))

print("\nWhat happens after that mess...")

for folder, subfolders, names in os.walk(my_images):
  for name in names:
    print(os.path.join(folder, name))

print(os.path.exists(os.path.join(my_images, "png file - not a gif.jpg")))
print(os.path.exists(os.path.join(my_images, "additional files/one last image.jpg")))
