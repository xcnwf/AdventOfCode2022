#!/usr/bin/env python3
p1 = 0
p2 = 0
import operator
from collections import deque
from functools import reduce
class Monkey:
	def __init__(self,starting_numbers,operation,condition,next_true,next_false):
		self.items=deque(starting_numbers)
		self.operation=operation
		self.condition = condition
		self.next_true = next_true
		self.next_false = next_false
		self.manipulations = 0

with open("../Inputs/d11.txt") as f:
	monkeys = []
	operations = {"+":operator.add,"*":operator.mul}
	while f.readline():
		starting_numbers = [int(x) for x in f.readline()[18:-1].split(', ')]

		(operation_str,b) = f.readline()[23:-1].split(" ")
		if b == "old":
			operation = lambda old,operation_str=operation_str: operations[operation_str](old,old)
		else:
			operation = lambda old,b=b,operation_str=operation_str: operations[operation_str](old, int(b))
		test = int(f.readline()[21:-1])

		next_true = int(f.readline()[29:-1])
		next_false = int(f.readline()[30:-1])

		monkeys.append(Monkey(starting_numbers,operation,lambda x,test=test: x % test == 0, next_true, next_false))

		#skip empty line
		f.readline()

for _ in range(20):
	for m in monkeys:
		while m.items:
			x = m.items.popleft()
			m.manipulations += 1
			x = m.operation(x) // 3
			monkeys[m.next_true if m.condition(x) else m.next_false].items.append(x)

""" m = monkeys[0]
while m.items:
	print(m.items,end=' ')
	x = m.items.popleft()
	print("=>",x)
	m.manipulations += 1
	print(f"Manipulations : {m.manipulations}")
	x = m.operation(x) // 3
	print(f"New x : {x}")
	print(f"Monkeys = {m.next_true} (True) / {m.next_false} (False)")
	next_monkey = m.next_true if m.condition(x) else m.next_false
	print(f"Next monkey : {next_monkey}")
	print()
	monkeys[m.next_true if m.condition(x) else m.next_false].items.append(x) """


monkeys.sort(key=lambda m:-m.manipulations)
p1 = reduce(operator.mul,map(lambda m:m.manipulations,monkeys[:2]))

if __name__ == "__main__":
	print(f"Part1: {p1}")
	print(f"Part2: {p2}")

