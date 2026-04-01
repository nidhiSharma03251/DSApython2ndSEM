"""1. F. Write a function that takes a list of integers as a parameters and
returns third smallest number from the list. For example,
input:[34,89,54,20,50,76,10,45,90] output: 34 """


def third_smallest(my_list):
	new_list = sorted(set(my_list))

	if len(new_list) <3:
		return None
	else:
		return new_list[2]

my_list = [34,89,54,20,50,76,10,45,90]
print(third_smallest(my_list))