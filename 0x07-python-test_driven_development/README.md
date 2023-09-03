# 0x07. Python - Test-driven development

This project focuses on the principles of Test-Driven Development (TDD) in Python. You will implement various Python functions and write tests for them, following TDD practices.

## Project Details

- **Author:** Guillaume
- **Weight:** 1
- **Start Date:** August 31, 2023, 6:00 AM
- **End Date:** September 6, 2023, 6:00 AM
- **Checker Release:** September 6, 2023, 6:00 AM
- **Auto Review Deadline:** At the project deadline

## Concepts

For this project, it's essential to understand the concept of "Never forget a test." You should prioritize writing documentation (module(s) + function(s)) and tests before writing the actual code. Collaborate on test cases to ensure comprehensive coverage while avoiding collaboration on code implementation.

## Background Context

Starting from today, you are expected to:

- Write documentation and tests first, based on task requirements, before coding.
- Intranet checks for Python projects will be released after the first deadline, allowing you to focus on TDD.
- Collaborate on test cases, but not on code implementation.
- Always consider all possible edge cases and do not trust user input.

## Resources

Read or watch the following resources:

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (until "26.2.3.7. Warnings" included)
- [doctest – Testing through documentation](https://docs.python.org/3/library/doctest.html)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)
- [Unittest module](https://docs.python.org/3/library/unittest.html)
- [Interactive and Non-interactive tests](https://docs.python.org/3/library/doctest.html#what-are-interactive-and-non-interactive-tests)

## Learning Objectives

By the end of this project, you should be able to:

- Explain why Python programming is awesome.
- Understand what an interactive test is.
- Recognize the importance of tests in software development.
- Write Docstrings to create tests.
- Write documentation for each module and function.
- Know the basic option flags to create tests.
- Identify and handle edge cases effectively.

## Copyright - Plagiarism

- You must develop solutions for the tasks yourself to meet the learning objectives.
- Copying and pasting someone else’s work is strictly forbidden and will result in removal from the program.
- Do not publish any content of this project.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation should be a real sentence explaining the purpose of the module, class, or method (the length will be verified)
- Collaborate on test cases to avoid missing any edge cases - The Checker checks for tests!

## Tasks

1. [Integers addition](./0-add_integer.py) - Write a function that adds 2 integers.
2. [Divide a matrix](./2-matrix_divided.py) - Write a function that divides all elements of a matrix.
3. [Say my name](./3-say_my_name.py) - Write a function that prints "My name is <first name> <last name>".
4. [Print square](./4-print_square.py) - Write a function that prints a square with the character `#`.
5. [Text indentation](./5-text_indentation.py) - Write a function that prints a text with 2 new lines after each of these characters: `.` , `?`, and `:`.
6. [Max integer - Unittest](./6-max_integer.py) - Write unittests for the `max_integer` function.

Feel free to adapt and expand this `README.md` as needed for your project documentation. Make sure to include the actual code and tests for each task in your project directory.

