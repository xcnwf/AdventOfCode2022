#!/usr/bin/env python3
p1 = 0
p2 = 0
with open("../Inputs/d10.txt") as f:
	next_cycle = 20
	cycle = 0
	x = 1
	CRT_lines = ["" for _ in range(6)]

	for l in f:
		prev_x = x
		if l.startswith("noop"):
			cycles_taken = 1
		elif l.startswith("addx"):
			x += int(l[5:-1])
			cycles_taken = 2

		for i in range(cycles_taken):
			CRT_lines[(cycle + i) // 40] += '#' if abs(((cycle + i) % 40) - prev_x) <= 1 else ' '
		cycle += cycles_taken

		if cycle >= next_cycle:
			p1 += next_cycle * prev_x
			next_cycle += 40

p2 = '\n' + '\n'.join(CRT_lines)

if __name__ == "__main__":
	print(f"Part1: {p1}")
	print(f"Part2: {p2}")

