#!/usr/bin/env python3

import re

new_map = []

# Read in file
with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

# Pull out numbers into list
for line in lines:
	eachline = re.findall(r"[\d]+", line)
	eachline = list(map(int, eachline)) 	# Convert list of strings to list of ints		
	new_map.append(eachline)

# Create blank grid/diagram populating with 0's
maxx, maxy = 0,0
for maxline in new_map:
	if maxline[0] > maxx or maxline[2] > maxx: maxx = max(maxline[0], maxline[2])
	if maxline[1] > maxy or maxline[3] > maxy: maxy = max(maxline[1], maxline[3])
grid = [[0 for i in range(maxx+1)] for j in range(maxy+1)]

# Add in straight lines
for entry in new_map:
	x1, y1, x2, y2 = entry[0], entry[1], entry[2], entry[3]
	if x1 == x2:
		for i in range(min(y1,y2), max(y1,y2)+1):
			grid[i][x1] += 1
	elif y1 == y2:
		for i in range(min(x1,x2), max(x1,x2)+1):
			grid[y1][i] += 1
# Diagonal condition
	elif abs(x1-x2) == abs(y1-y2):
		if x1 < x2 and y1 < y2: # Increase X and Increase Y
			for _ in range(x1, x2+1):
				grid[y1][x1] += 1
				x1 += 1
				y1 += 1
		elif x1 < x2 and y1 > y2: # Increase X and Decrease Y ##########
			for _ in range(x1, x2+1):
				grid[y1][x1] += 1
				x1 += 1
				y1 -= 1
		elif x1 > x2 and y1 > y2: # Decrease X and Decrease Y
			for _ in range(y2, y1+1):
				grid[y1][x1] += 1
				x1 -= 1
				y1 -= 1
		elif x1 > x2 and y1 < y2: # Decrease X and Increase Y
			for _ in range(y1, y2+1):
				grid[y1][x1] += 1
				x1 -= 1
				y1 += 1

# Count all entries > 1
count = 0
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] > 1: count += 1
		
print(count)