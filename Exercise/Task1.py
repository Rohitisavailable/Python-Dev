"""
Task - Student Information Management System

This module demonstrates object-oriented programming concepts including:
- Class creation with __init__ constructor method
- Instance methods and data encapsulation
- User input handling and validation
- Method chaining and output formatting

Classes:
    Student: Represents a student with personal and academic information

Functions:
    N/A (This is a class-based implementation)

Attributes:
    name (str): The student's full name
    age (int): The student's age in years
    marks (float): The student's academic marks/score

Methods:
    __init__(name, age, marks): Constructor to initialize student object
    display(): Instance method to print all student attributes

Example:
    >>> student1 = Student("John Doe", 20, 85.5)
    >>> student1.display()
    
    >>> student2 = Student("Jane Smith", 19, 92.0)
    >>> student2.display()

Note:
    - Multiple objects can be created with different parameters
    - Demonstrates the use of arguments and parameters in class instantiation
    - Each object maintains its own independent state
"""

#n = input("Name: ")
#a = int(input("Age: "))
#m = int(input("Marks: "))

class Student:

    def __init__(self, n , a, **m):
        self.name = n
        self.age = a
        self.marks = m
    
    def Display(self):
        print("Hi", self.name)
        print("Your age is ", self.age)
        print("you scored ", self.marks)

s1 = Student("Rohit", 23, maths=93, english=65, science=23)

s1.Display()
