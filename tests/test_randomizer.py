# This allows for importing files/modules from a different directory
import sys
sys.path.insert(0, 'methods')

from randomizer import select_random_student

import pytest

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
  returned_groups = select_random_student(list_of_students, 3)
  print(returned_groups)
  assert len(returned_groups) == 3
  # TODO: Figure out how to verify groups of three

