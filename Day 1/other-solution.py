#!/usr/bin/env python3

with open('input.txt', 'r') as f:
	data = f.readlines()
	result = 0
	for index, line in enumerate(data):
		if index == 0:
			prev = int(line)
			continue
		
		if int(line) > prev:
			result += 1
		prev = int(line)
		
	print(result)