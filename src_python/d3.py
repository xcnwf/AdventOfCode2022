#!/usr/bin/env python3
with open("../Inputs/d3.txt") as f:
    policies = [[ord(c)-0x60 + ((0x20+26) if ord(c) < 0x60 else 0) for c in l.strip()] for l in f]

p1=sum(sum(set(l[len(l)//2:]) & set(l[:len(l)//2])) for l in policies)

p2 = sum(sum(set(policies[3*i]) & set(policies[3*i+1]) & set(policies[3*i+2])) for i in range(len(policies)//3))

if __name__=="__main__":
    print(f"Part1 : {p1}")
    print(f"Part2 : {p2}")