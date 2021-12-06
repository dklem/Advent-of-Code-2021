#!/usr/bin/env python3

# Read in file into lines list

def create_boards():
	with open('input-demo.txt', 'r') as f:
		lines = f.read().splitlines()
	
	order = lines[0].split(",")
	#print(order)
	
	rows = []
	
	for line in lines:
		if len(line) > 2:
			rows.append(line.split())
	print(rows)

create_boards()