import random

def select_random_student(some_list, number_of_students_in_each_group):
  group = []
  count = 0

  while count < number_of_students_in_each_group:
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