#!/usr/bin/env python3

# Read in file
with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

ylength = len(lines)
xlength = len(lines[0])

low_points = []

for y in range(0,ylength):
	for x in range(0,xlength):
		up = lines[y-1][x] if y != 0 else 10
		down = lines[y+1][x] if y != ylength-1 else 10
		right = lines[y][x+1] if x != xlength-1 else 10
		left = lines[y][x-1] if x != 0 else 10		
		point = int(lines[y][x])
		
		if all(point < int(i) for i in (up, down, right, left)):
			low_points.append(point)

risk_level = sum(low_points) + len(low_points)
print (f"Risk Level: {risk_level}")