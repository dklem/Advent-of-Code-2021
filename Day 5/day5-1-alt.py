#!/usr/bin/env python3

import re

def create_grid():
	maxx, maxy = 0,0
	for line in lines:
		maxline = re.findall(r"[\d]+", line)
		maxline = list(map(int, maxline))
		if maxline[0] > maxx or maxline[2] > maxx: maxx = max(maxline[0], maxline[2])
		if maxline[1] > maxy or maxline[3] > maxy: maxy = max(maxline[1], maxline[3])
	return [[0 for i in range(maxx+1)] for j in range(maxy+1)]

def create_line(x1,y1,x2,y2):
	if x1 == x2:
		for i in range(min(y1,y2), max(y1,y2)+1):
			grid[i][x1] += 1
	elif y1 == y2:
		for i in range(min(x1,x2), max(x1,x2)+1):
			grid[y1][i] += 1
	return grid

with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

grid = create_grid()

for line in lines:
	eachline = re.findall(r"[\d]+", line)
	eachline = list(map(int, eachline)) 	# Convert list of strings to list of ints

	if eachline[0] == eachline[2] or eachline[1] == eachline[3]:
		grid = create_line(x1=eachline[0],y1=eachline[1],x2=eachline[2],y2=eachline[3])

count = 0
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] > 1: count += 1

print(count)