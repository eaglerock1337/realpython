def enrollment_stats(unis):
  students = []
  tuition = []
  for university in unis:
    students.append(university[1])
    tuition.append(university[2])
  return students, tuition

def mean(numbers):
  sumup = 0
  for i in numbers:
    sumup += i
  return int(sumup / len(numbers))

def median(numbers):
  numbers.sort()
  return numbers[int(len(numbers) / 2)] 

universities = [
  ['California Institute of Technology', 2175, 37704],
  ['Harvard', 19627, 39849],
  ['Massachusetts Institute of Technology', 10566, 40732],
  ['Princeton', 7802, 37000],
  ['Rice', 5879, 35551],
  ['Stanford', 19535, 40569],
  ['Yale', 11701, 40500]
]

students_list, tuition_list = enrollment_stats(universities)

studentsum = sum(students_list)
tuitionsum = sum(tuition_list)
smean = mean(students_list)
smedian = median(students_list)
tmean = mean(tuition_list)
tmedian = median(tuition_list)

print("*************************")
print("Total Students:   {}".format(studentsum))
print("Total tuition:  $ {}".format(tuitionsum))
print()
print("Student mean:     {}".format(smean))
print("Student median:   {}".format(smedian))
print()
print("Tuition mean:     {}".format(tmean))
print("Tuition median:   {}".format(tmedian))
print("*************************")
