#!/usr/bin/env python3

# Read in file
with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

count = 0

for line in lines:
	eachline = line.split("|")
	output_values = eachline[1].split(" ")
	for i in output_values:
		if len(i) in (2,3,4,7):
			count += 1

print(count)