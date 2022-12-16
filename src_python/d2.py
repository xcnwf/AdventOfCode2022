#!/usr/bin/env python3
with open("../Input/d2.txt") as f:
    lines = [(ord(l[0])-0x40,ord(l[2])-0x40-23) for l in f]

p1 = 0
for (a,p) in lines:
    p1 += p + 3*((p-a+1)%3)


p2 = 0
for (a,p) in lines:
    p2 += 3*((p-1)) + (a+p)%3 + 1

if __name__ == "__main__":
    print(f"Part1 : {p1}")
    print(f"Part2 : {p2}")

