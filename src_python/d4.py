#!/usr/bin/env python3
p1=0
p2=0

with open("../Inputs/d4.txt") as f:
    for l in f:
        places = l.strip().split(",")
        x1,y1 = (int(x) for x in places[0].split("-"))
        x2,y2 = (int(x) for x in places[1].split("-"))
        p1+=(x1-x2)*(y1-y2) <= 0
        p2+=(y1>=x2)&(y2>=x1)
        
if __name__=="__main__":
    print(f"Part1 : {p1}")
    print(f"Part2 : {p2}")