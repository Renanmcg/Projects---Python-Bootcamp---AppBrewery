# List comprehension
# With numbers
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

# With strings
name = 'Renan'
new_list = [letter for letter in name]
print(new_list)  # each letter become an element of the list

# Doing a list with doubles
double = [n * 2 for n in range(0, 5)]
print(double)

# Conditional list comprehension
names = ['Charles', 'Jean', 'Dave', 'Pedro', 'Getúlio']
short_names = [name for name in names if len(name) < 6]
print(short_names)

names = ['Charles', 'Jean', 'Dave', 'Pedro', 'Getúlio']
long_names = [name.upper() for name in names if len(name) > 6]
print(long_names)

# Exercise 1: Squaring Numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# Exercise 2 - Data Overlap

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]
print(result)  # only even numbers

# Exercise 3 is in another folder


# Dictionary Comprehension

# Dictionary with names and notes
from random import randint
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_score = {student:randint(1, 100) for student in names}
print(students_score)

passed_students = {student:note for (student, note) in students_score.items() if note >= 60}
print(passed_students)

# Exercise 4 - Dictionary Comprehension

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

print(result)

# Exercise 5 is in another folder

