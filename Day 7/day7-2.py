#!/usr/bin/env python3

from operator import add
import math

# Read in file, split into list
with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
	data = lines[0].split(",")
	data = list(map(int, data))

least_fuel = 0

for i in range(0, max(data)+1):
	point = [-i] * len(data)
	newdata=list(map(add,data,point))

	fuel = 0

	for steps in newdata:
		fuel += (abs(steps)*abs(steps) + abs(steps))/ 2
	
	if fuel < least_fuel or least_fuel == 0:
		least_fuel = fuel
	
#	print(f"This Run: {fuel}, Least: {least_fuel}")
		
print(int(least_fuel))