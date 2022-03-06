# This allows for importing files/modules from a different directory
import sys
sys.path.insert(0, 'methods')

from randomizer import select_random_student

import pytest
import copy

@pytest.fixture
def empty_list():
  return []

@pytest.fixture
def list_of_students():
  return ['tom', 'joe', 'chris', 'mary', 'john', 'jane']

# use case : list is empty
def test_select_random_student(empty_list):
  assert select_random_student(empty_list, 4) == []

# use case : create groups of 3
def test_select__random_student(list_of_students):
  original_student_list = copy.deepcopy(list_of_students)
  returned_group = select_random_student(list_of_students, 3)
  
  # asserts the length of returned list has 3 students
  assert len(returned_group) == 3
  # asserts all the students in the returned_group exist in the original_student_list
  assert all(student in original_student_list for student in returned_group)
  # asserts the returned_group students + the remaining students in list_of_students make up the entire original_student_list
  assert sorted(original_student_list) == sorted(returned_group + list_of_students)
