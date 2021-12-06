#!/usr/bin/env python3
import os

# Read each line of file, strip newline, place into list called "lines"
with open('input.txt', 'r') as input_file:
	lines = input_file.read().splitlines()
	
increased = 0
decreased = 0
index = 0

for current_number in lines:

#	print(f"Number is {i}")
	if index == 0:
		print(f"{current_number} (N/A - No previous measurement)")
	else:
#		if current_number > previous_number: 
# WRONG, see https://www.reddit.com/r/adventofcode/comments/r6h1tm/day_1_part_1_help_python/
		if int(current_number) > int(previous_number):
			change = "increased"
			increased += 1
			print (f"{current_number} {previous_number} increased {increased}")
		else:
			change = "decreased"
			decreased += 1
#		print(f"{current_number} ({change} - Previous number is {previous_number})")
	index += 1
	previous_number = lines[index-1]

print(f"Increased = {increased}")
print(f"Decreased = {decreased}")

# 