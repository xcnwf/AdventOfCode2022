#!/usr/bin/env python3
p1 = 0
p2 = 0

def distance(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def solve_circle_y_intersection(center,radius,y):
    if abs(y - center[1]) > radius:
        return None
    else: 
        x = abs(abs(y-center[1]) - radius)
        return (center[0]-x,center[0]+x)

circles = []
with open("../Inputs/d15.txt") as f:
    for line in f:
        s1, s2 = line.strip().split(": ")
        station, beacon = [(int(s[s.index("x=")+2:s.index(",")]), int(s[s.index("y=")+2:]))
                                for s in (s1,s2)]
        circle = (station,abs(station[0]-beacon[0]) + abs(station[1] - beacon[1]))
        circles.append(circle)

intervals = []
for (center, radius) in circles:
    res = solve_circle_y_intersection(center, radius, 2000000)
    if res:
        x_low,x_high = res
    else:
        continue

    # This is a weird idea I had to work on intervals
    min_ind = max((i for i,(_,x2) in enumerate(intervals) if x2 < x_low),default=-1)+1
    max_ind = max((i for i,(x1,_) in enumerate(intervals) if x1 <= x_high),default=-1)+1
    #print(intervals, res, min_ind, max_ind)

    if min_ind == max_ind:
        intervals.insert(min_ind, (x_low,x_high))
    else:
        intervals[min_ind:max_ind] = [(min(x_low,intervals[min_ind][0]),max(x_high,intervals[max_ind-1][1]))]

p1 = sum(x2-x1 for x1,x2 in intervals)




#Part2: Must be at the "center" of all beacons
if __name__ == "__main__":
    print(f"Part1 : {p1}")
    print(f"Part2 : {p2}")