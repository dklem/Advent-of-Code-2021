#!/usr/bin/env python3

# Read in file into lines list
with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

# Initialize the result list, calculating the length of each line to get the right size
result = [0] * len(lines[0])

for line in lines:
	position=0
	for i in line:
		if int(i) == 0:
			result[position] -= 1
		if int(i) == 1:
			result[position] += 1
		position += 1
print(result)

gamma = ''
epsilon = ''

for j in result:
	if int(j) > 0:
		gamma += '1'
		epsilon += '0'
	elif int(j) < 0:
		gamma += '0'
		epsilon += '1'

# Print out gamma/epsilon both in binary and decimal
print(f"gamma:   {gamma}, {int(gamma,2)}")
print(f"epsilon: {epsilon}, {int(epsilon,2)}")

power_consumption = int(gamma,2) * int(epsilon, 2)
print(f"power:   {power_consumption}")