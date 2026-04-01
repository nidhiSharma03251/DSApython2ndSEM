## 1.A. Write a program to print first 5 character of your name using for loop.

name=input("Enter your name: ")
for i in range(5):
	print(name[:i+1])







"""The python Command
The python command is used outside of a Python script, in your computer's terminal or command line.  It starts the Python interpreter and tells your operating system to run a Python program.

Purpose: To execute a complete Python script file. 
Usage: python script_name.py
Scope: A system-level command.


The import Command
The import command is used inside a Python script.  It loads another Python module (a file containing Python code) into the current script, making its functions, classes, and variables available for use. 
	
Purpose: To bring code from one Python file (module) into another. 
Usage: import module_name or from module_name import function_name
Scope: A Python language statement for code organization and reuse
In essence, you use the python command to run a program, and you use the import statement within that program to use code from other files. """