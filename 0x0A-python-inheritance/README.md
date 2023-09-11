0x0A. Python - Inheritance
Table of Contents
Introduction
Learning Objectives
Requirements
Tasks
Task 0: Lookup
Task 1: My List
Task 2: Exact Same Object
Task 3: Same Class or Inherit From
Task 4: Only Sub Class Of
Task 5: Geometry Module
Task 6: Improve Geometry
Task 7: Integer Validator
Task 8: Rectangle
Task 9: Full Rectangle
Task 10: Square #1
Task 11: Square #2
Introduction
This project focuses on Python programming with an emphasis on inheritance in object-oriented programming (OOP). You'll explore concepts related to classes, subclasses, inheritance, and more.

Learning Objectives
By completing this project, you will be able to:

Explain the awesomeness of Python programming.
Understand what superclass, base class, and parent class mean.
Define subclasses and understand when an instance can have new attributes.
Inherit a class from another and deal with multiple base classes.
Recognize the default class that every class inherits from.
Override methods or attributes inherited from base classes.
Work with attributes and methods available to subclasses by inheritance.
Understand the purpose of inheritance in OOP.
Utilize isinstance, issubclass, type, and super built-in functions.
Ensure code quality and adhere to PEP 8 style guidelines.
Requirements
Python Scripts
Editors: vi, vim, emacs
Interpretation/Compilation: Python 3.8.5
All files should end with a new line.
The first line of all files should be #!/usr/bin/python3.
A README.md file is mandatory at the root of the project folder.
Code should adhere to PEP 8 style guidelines.
All files must be executable.
Python Test Cases
Editors: vi, vim, emacs
All test files should end with a new line.
All test files should be inside a folder named tests.
Test files should have a .txt extension.
Run tests using the command: python3 -m doctest ./tests/*
Modules, classes, and functions should have documentation.
Documentation
Do not use the words "import" or "from" inside your comments.
Tasks
Task 0: Lookup
Write a function lookup(obj) that returns the list of available attributes and methods of an object. You are not allowed to import any module.

Task 1: My List
Write a class MyList that inherits from the list class. It should have a public instance method print_sorted(self) that prints the list sorted in ascending order. You can assume that all elements of the list will be of type int. You are not allowed to import any module.

Task 2: Exact Same Object
Write a function is_same_class(obj, a_class) that returns True if the object is exactly an instance of the specified class; otherwise, it returns False. You are not allowed to import any module.

Task 3: Same Class or Inherit From
Write a function is_kind_of_class(obj, a_class) that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise, it returns False. You are not allowed to import any module.

Task 4: Only Sub Class Of
Write a function inherits_from(obj, a_class) that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise, it returns False. You are not allowed to import any module.

Task 5: Geometry Module
Write an empty class BaseGeometry. You are not allowed to import any module.

Task 6: Improve Geometry
Write a class BaseGeometry (based on Task 5) with a public instance method area(self) that raises an Exception with the message area() is not implemented. You are not allowed to import any module.

Task 7: Integer Validator
Write a class BaseGeometry (based on Task 6) with a public instance method integer_validator(self, name, value) that validates the value. If value is not an integer, it raises a TypeError exception with the message <name> must be an integer. If value is less than or equal to 0, it raises a ValueError exception with the message <name> must be greater than 0. You are not allowed to import any module.

Task 8: Rectangle
Write a class Rectangle that inherits from BaseGeometry. It should have an instantiation method __init__(self, width, height) where width and height must be positive integers, validated by integer_validator. These attributes should be private with no getter or setter methods.

Task 9: Full Rectangle
Write a class Rectangle (based on Task 8) with the area() method implemented. The print() method should print and str() should return the rectangle description in the format [Rectangle] <width>/<height>.

Task 10: Square #1
Write a class Square that inherits from Rectangle (based on Task 9). It should have an instantiation method __init__(self, size) where size must be a positive integer, validated by integer_validator. The print() method should print and str() should return the square description in the format [Rectangle] <size>/<size>.

Task 11: Square #2
Write a class Square (based on Task 10) with the area() method implemented. The print() method should print and str() should return the square description in the format [Square] <size>/<size>.
