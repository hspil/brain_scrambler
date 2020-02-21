#!/usr/bin/python
########################################################################
#	Brain Scrambler
#	
#	*	Tihs porgarm is for gneienartg txet lkie tihs
#	*	Arpneltpay the biran can unrdntased sftuf lkie tihs
#
########################################################################


import random
import re


def main(args):
	#split into list of words, punctuation, and whitespace
	words = re.findall(r"\w+|[^\w]|\s", sys.stdin.read()[:-1], 
	re.UNICODE)
	
	for word in words:
		#scramble if solely alphabetic and longer than 3 characters
		if re.fullmatch('^[a-zA-Z]{4,}$', word):
			#split  word to char list
			letters = list(word)
			
			middle = letters[1:-1]
			random.shuffle(middle)
			
			#reconcatenate first     middle            last letters
			word = str(letters[0]) + "".join(middle) + str(letters[-1])
		
		#print 
		print(word, end = "")
		
	print('')
			
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
