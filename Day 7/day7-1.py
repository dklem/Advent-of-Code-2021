#!/usr/bin/env python3

from operator import add

# Read in file, split into list
with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
	data = lines[0].split(",")
	data = list(map(int, data))

least_fuel = sum(data)

for i in range(0, max(data)+1):
	point = [-i] * len(data)
	newdata=list(map(add,data,point))
	fuel = sum(map(abs, newdata))
#	print(fuel, newdata)
	
	if fuel < least_fuel:
		least_fuel = fuel

print(least_fuel)