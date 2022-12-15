#!/usr/bin/env python3
p1=0
p2=0
with open("../Inputs/d6.txt") as f:
    for l in f:
        pos=4
        while pos < len(l):
            subl = set(l[pos-4:pos])
            if len(subl)==4:
                break
            pos += 1
        p1+=pos
        pos=0
        while pos < len(l):
            subl = set(l[pos-14:pos])
            if len(subl)==14:
                break
            pos += 1
        p2+=pos
        
if __name__=="__main__":
    print(f"Part1 : {p1}")
    print(f"Part2 : {p2}")