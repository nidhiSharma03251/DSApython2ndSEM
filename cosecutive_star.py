"""1.E. Write a function that takes a string as a parameter and returns a string
with every successive repetitive character replaced with a star(*). For
example, ‘balloon’ is returned as ‘bal*o*n’."""

def change_star(str):
	new_str = ""	
	for ch in str:
		if ch not in new_str:
			new_str += ch
		else:
			new_str += "*"
	return new_str

str = input("Enter a string: ")
print(change_star(str))