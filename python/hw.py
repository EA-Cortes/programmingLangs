def word_smith(s, s2):
	# return will be a counting integer with the words that fit the criteria
	ret = 0

	# Get the letters from the second string
	letters = []
	for letter in s2:
		if(letter.isalpha()):
			letters.append(letter)

	# Split the first string into words
	substring = []
	substring = s.split()
	for word in substring:
		
		# get words that are more than 3 chars
		if(len(word) > 3):
			
			# Check if words start with vowel or contains letter from subset
			if(subString(word, letters)):
				
				# Match found, add to word_smith
				ret += 1
	return ret


# Helper function to see if word fits the criteria 
def subString(list1, list2):
	# Check if word contains letter
	for letter in list1:
		if letter in list2:
			return True
	
	# Check if first letter is a vowel
	first = list1[0]
	if first in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
		return True
	else:
		return False


def base_builder(input):
	# Counter variable that returns the sum of the quartary integers
	sum = 0
	# String that will output number in quartary
	quart = ""
	
	
	# algorithm to convert decimal number into quartary
	next = input
	while next > 0:
		if((next%4) == 0):
			quart = quart +  str(next%4)
		else:
			sum += (next%4)
			quart = quart +  str(next%4)
		next = next/4

	# Reverses the quart string
	quart = reverse(quart)

	# Prepares the return value
	ret = (sum, int(quart))
	return ret

# Helper function to output the string in quartary
def reverse(s):
	str =""
	for i in s:
		str = i + str
	return str