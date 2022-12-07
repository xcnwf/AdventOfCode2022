#!/usr/bin/env python3
with open("../Inputs/d1.txt") as f:
    max_values = [0]*3
    current_value = 0
    for l in f:
        if l.strip() == "":
            if current_value > max_values[0]:
                max_values[0] = current_value
                max_values.sort()
            current_value = 0
        else:
            current_value += int(l.strip())
    p1 = max_values[2]
    p2 = sum(max_values)

if __name__=="__main__":
    print(f"Part1 : {p1}")
    print(f"Part2 : {p2}")