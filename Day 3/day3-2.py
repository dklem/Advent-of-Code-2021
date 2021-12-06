#!/usr/bin/env python3

# Read in file into lines list
with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

# Oxygen generator rating
for i in range(0,len(lines[0])):
	working_set_zero = []
	working_set_one = []
	for line in lines:
		if int(line[i]) == 0:
			working_set_zero.append(line)
		if int(line[i]) == 1:
			working_set_one.append(line)
	
	if len(working_set_zero) > len(working_set_one) and len(working_set_zero) != 0:
		lines = working_set_zero
	elif len(working_set_zero) <= len(working_set_one) and len(working_set_one) != 0:
		lines = working_set_one

oxygen_rating = int(lines[0],2)
print(f"Oxygen Rating: {oxygen_rating}")


# CO2 scrubber rating

with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

for i in range(0,len(lines[0])):
	working_set_zero = []
	working_set_one = []
	for line in lines:
		if int(line[i]) == 0:
			working_set_zero.append(line)
		if int(line[i]) == 1:
			working_set_one.append(line)

	if len(working_set_zero) <= len(working_set_one) and len(working_set_zero) != 0:
		lines = working_set_zero
	elif len(working_set_zero) > len(working_set_one) and len(working_set_one) != 0:
		lines = working_set_one

scrubber_rating = int(lines[0],2)
print(f"CO2 Scrubber Rating: {scrubber_rating}")
print(f"Life Support Rating: {scrubber_rating*oxygen_rating}")
