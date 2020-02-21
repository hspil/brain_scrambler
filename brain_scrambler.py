#!/usr/bin/python
########################################################################
#	Brain Scrambler
#	
#	*	Tihs porgarm is for gneienartg txet lkie tihs
#	*	Arpneltpay the biran can unrdntased sftuf lkie tihs
#
########################################################################


import random

def main(args):
	#read text from stdin, trim trailing newline, and split into a list
	#at word boundaries
	words = sys.stdin.read()[:-1].split(" ")
	for word in words:
		letters = list(word)
		middle = letters[1:-1]
		random.shuffle(middle)
		print(str(letters[0]) + "".join(middle) + str(letters[-1]),
		end = " ")
			
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
