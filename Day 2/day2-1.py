#!/usr/bin/env python3

horizontal = 0
depth = 0

# 1. Read through file
with open('input.txt', 'r') as f:
	# Split lines
	lines = f.read().splitlines()
	# Read each line	
	for i in lines:
		# Split on whitespace, and save each into "direction" and "units"
		direction,units=i.split()
		if direction == "forward":
			horizontal += int(units)
		elif direction == "down":
			depth += int(units)
		elif direction == "up":
			depth -= int(units)

print (f"Forward = {horizontal}, Depth = {depth}")
print (f"Answer = {horizontal*depth}")