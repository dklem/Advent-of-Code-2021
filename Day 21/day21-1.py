#!/usr/bin/env python3

with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

p1_score, p2_score = 0, 0
turn = 0

p1_position = int(lines[0][-1])
p2_position = int(lines[1][-1])
board = [1,2,3,4,5,6,7,8,9,10]

while p1_score < 1000 and p2_score < 1000:

	turn += 1
	first_number = (turn*6-5)
	p1_position = (first_number + first_number + 1 + first_number + 2 + p1_position) % 10
	p2_position = (first_number + 3 + first_number + 4 + first_number + 5 + p2_position) % 10
	
	if p1_position == 0:
		p1_position = 10
	if p2_position == 0:
		p2_position = 10
	
	p1_score += p1_position
	p2_score += p2_position
	
#	print(f"Player 1 moves to space {p1_position} for a total score of {p1_score}")
#	print(f"Player 2 moves to space {p2_position} for a total score of {p2_score}")

roll = (turn) * 6

if p1_score >= 1000:
	p2_score -= p2_position
	roll -= 3
	
print(min(p1_score, p2_score)*roll)