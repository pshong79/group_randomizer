# This allows for importing files/modules from a different directory
import sys
sys.path.insert(0, 'methods')

from randomizer import select_random_student

class_list = [ 
            'john', 'sally', 'thomas', 
            'peter', 'jenny', 'luke',
            'stephanie', 'katie', 'joseph', 
            'matthew', 'bobby', 'mike',
            'will', 'christine', 'lisa',
            'laura', 'josh', 'alex'
           ]
student_groups = []
team_number = 1

while (len(class_list) > 0):
  student_groups = select_random_student(class_list)
  # Python3
  print(f'team {team_number}: {student_groups}')
  # Python2
  # print('team' + str(team_number) + ': ' + str(student_groups))
  team_number += 1
