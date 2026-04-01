""" 1.C. Write a program that create a dictionary with the frequency of the
vowels from an inputted string. For example: input:’institute’.
Output:{‘i’:2,’u’:1,’e’:1} """

def count_vowel(word):
	vowels = 'aeiou'
	vowel_count = {v:0 for v in vowels}
	
	word = word.lower()
	
	for char in word:
		if char in vowel_count:
			vowel_count[char]+=1
	
	vowel_count = {k: v for k,v in vowel_count.items() if v>0}
	return vowel_count


word = "institute"
print(count_vowel(word))	