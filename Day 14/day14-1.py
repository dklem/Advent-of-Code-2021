#!/usr/bin/env python3

steps = 10

with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
	initial_string = lines[0]

mapping = {}

for line in lines:
	if '->' in line:
		x,y=line.split(" -> ")
		replacement_text = x[0]+y
		mapping[x] = replacement_text

for _ in range(1, steps+1):
	processed_string = ''
	for i in range(0, len(initial_string)):
		if i == len(initial_string)-1:
			processed_string += initial_string[i]
		else:
			pair = initial_string[i]+initial_string[i+1]
			processed_string += mapping[pair]
	initial_string = processed_string

unique = list(set(processed_string))

values = []

for letter in unique:
	values.append(processed_string.count(letter))

print(f"{max(values)} - {min(values)} = {max(values)-min(values)}")