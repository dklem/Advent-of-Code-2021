#!/usr/bin/env python3
import os

# Read each line of file, strip newline, place into list called "lines"
with open('input.txt', 'r') as input_file:
	lines = input_file.read().splitlines()
	
increased = 0
decreased = 0
equal = 0
index = 0

#print (len(lines))

for i in range(0, len(lines)-2):
	line1 = int(lines[i-1])
	line2 = int(lines[i])
	line3 = int(lines[i+1])
	line4 = int(lines[i+2])
	
	set1 = line1 + line2 + line3
	set2 = line2 + line3 + line4
	
	if int(set2) > int(set1):
		print(f"{set1} - {set2} (increased)")
		increased += 1
	elif set2 == set1:
		print(f"{set1} - {set2} (no change)")
		equal += 1
	else:
		print(f"{set1} - {set2} (decreased)")
		decreased += 1

print(f"Increased = {increased}")
print(f"Decreased = {decreased}")
print(f"Equal = {equal}")