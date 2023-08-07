Tasks
0. Run Python file (Mandatory)
Write a Shell script that runs a Python script. The Python file name will be saved in the environment variable $PYFILE.

bash
Copy code
# Contents of main.py
#!/usr/bin/python3
print("Best School")
To run the script:

bash
Copy code
export PYFILE=main.py
./0-run
Expected Output:

Copy code
Best School
1. Run inline (Mandatory)
Write a Shell script that runs Python code. The Python code will be saved in the environment variable $PYCODE.

bash
Copy code
export PYCODE='print(f"Best School: {88+10}")'
./1-run_inline
Expected Output:

yaml
Copy code
Best School: 98
2. Hello, print (Mandatory)
Write a Python script that prints exactly "Programming is like building a multilingual puzzle," followed by a new line.

bash
Copy code
./2-print.py
Expected Output:

css
Copy code
"Programming is like building a multilingual puzzle
3. Print integer (Mandatory)
Complete this source code to print the integer stored in the variable number, followed by "Battery street," followed by a new line.

bash
Copy code
./3-print_number.py
Expected Output:

Copy code
98 Battery street
4. Print float (Mandatory)
Complete the source code to print the float stored in the variable number with a precision of 2 digits.

bash
Copy code
./4-print_float.py
Expected Output:

css
Copy code
Float: 3.14
5. Print string (Mandatory)
Complete this source code to print the value of the variable str three times, followed by a new line, and then the first 9 characters of str, followed by a new line.

bash
Copy code
./5-print_string.py 
Expected Output:

Copy code
Holberton SchoolHolberton SchoolHolberton School
Holberton
6. Play with strings (Mandatory)
Complete this source code to print "Welcome to Holberton School!".

bash
Copy code
./6-concat.py
Expected Output:

css
Copy code
Welcome to Holberton School!
7. Copy - Cut - Paste (Mandatory)
Complete this source code to print specific substrings from the variable word.

bash
Copy code
./7-edges.py
Expected Output:

yaml
Copy code
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
8. Create a new sentence (Mandatory)
Complete this source code to print "object-oriented programming with Python", followed by a new line.

bash
Copy code
./8-concat_edges.py
Expected Output:

csharp
Copy code
object-oriented programming with Python
9. Easter Egg (Mandatory)
Write a Python script that prints "The Zen of Python, by Tim Peters," followed by a new line.

bash
Copy code
./9-easter_egg.py
Expected Output:

vbnet
Copy code
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...
...
Namespaces are one honking great idea -- let's do more of those!
10. Linked list cycle (Mandatory)
Write a function in C that checks if a singly linked list has a cycle in it.

Prototype: int check_cycle(listint_t *list);
Return: 0 if there is no cycle, 1 if there is a cycle

Requirements:

Only these functions are allowed: write, printf, putchar, puts, malloc, free




