#!/usr/bin/env python3

def translate(character):
	if character in opening:
		return(closing[opening.index(character)])
	if character in closing:
		index = closing.index(character)
		return(opening[closing.index(character)])

	
def calculate_score(char_list):
	score=0
	for i in char_list:
		score *= 5
		if i == ")": score += 1
		if i == "]": score += 2
		if i == "}": score += 3
		if i == ">": score += 4
	return(score)
		
	
# Read in file
with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
	
opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']

finish = []
scores = []

for line in lines:
	open_chars = []
	finish = []
	done = False
	for char in line:
		if not done:
			if char in opening:
				open_chars.append(char)
			elif char in closing:
				expected_close = translate(open_chars[-1])
				if expected_close != char:
					done = True
				else:
					open_chars.pop(-1)
	if done != True:
		open_chars.reverse()
		for j in open_chars:
			finish.append(translate(j))
		
		scores.append(calculate_score(finish))

scores.sort()
print(scores[int(len(scores)/2)])