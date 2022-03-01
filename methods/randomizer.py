import random

def select_random_student(some_list):
  group = []
  # if you want groups of four, change the next line to a 4 and so on...
  group_size = 3
  count = 0

  while count < group_size:
    if (len(some_list) > 0):
      student = random.choice(some_list)
      group.append(student)
      some_list.remove(student)
      count += 1
    # else if some_list is empty, kick out of the while-loop
    else:
      break
  # this returns the list of students in one group
  return group