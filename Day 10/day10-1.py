#!/usr/bin/env python3

def translate(character):
	if character in opening:
		return(closing[opening.index(character)])
	if character in closing:
		index = closing.index(character)
		return(opening[closing.index(character)])
		
# Read in file
with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']

illegal = []
score = 0

for line in lines:
	open_chars = []
	done = False
	for char in line:
		if not done:
			if char in opening:
				open_chars.append(char)
			elif char in closing:
				expected_close = translate(open_chars[-1])
				if expected_close != char:
#					print(f"Expected {expected_close}, but found {char} instead")
					illegal.append(char)
					done = True
				else:
					open_chars.pop(-1)

for i in illegal:
	if i == ")":
		score += 3
	elif i == "]":
		score += 57
	elif i == "}":
		score += 1197
	elif i == ">":
		score += 25137

print(score)