# Description: 
This program was created to provide a way for my wife, an educator, to quickly place her students in groups at random.

The program takes a list of students in a class and places them randomly in groups. The size of the group is determined by the variable `group_size`. After creating the group of specified `group_size`, the program, then, prints all the groups to the console.

This program is able to handle any size groups regardless of if the number of students in `class_list` is evenly divisible by `group_size` or not.

## To Run:
To run the program, in console, use the command:
```python
$ python app.py
```


## To Run Tests:
To run the tests, in console, in the root directory, use the command:
```python
$ pytest <path_to_directory_or_file> -v
```
The `-v` is optional and provides more information from the test run.