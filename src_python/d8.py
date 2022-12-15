#!/usr/bin/env python3
p1 = 0
p2 = 0
with open("../Inputs/d8_small.txt") as f:
    forest: [[int]] = [[int(i) for i in line[:-1]] for line in f]

width = len(forest[0])
height = len(forest)


#p1 = visible
visible = set()
#p2 = score

scores = [[1 for j in range(width)] for i in range(height)]

for i in range(1,height-1):
    left: int = forest[i][0]
    view_dist = 0
    last = [0 for _ in range(10)]
    for j in range(1,width-1):
        tree = forest[i][j]
        if tree > left:
            visible.add((i,j))
            left = tree
        
        scores[i][j] *= j-max(last[tree:])
        last[tree] = j

    right = forest[i][-1]
    last = [width-1 for _ in range(10)]
    for j in range(width-2, 0,-1):
        tree = forest[i][j]
        if tree > right:
            visible.add((i,j))
            right = tree
        
        scores[i][j] *= min(last[tree:]) - j
        last[tree] = j

for j in range(1,width-1):
    up = forest[0][j]
    last = [0 for _ in range(10)]
    for i in range(1,height-1):
        tree = forest[i][j]
        if tree > up:
            visible.add((i,j))
            up = tree

        scores[i][j] *= i - max(last[tree:])
        last[tree] = i

    down = forest[-1][j]
    last = [height-1 for _ in range(10)]
    for i in range(height-2, 0,-1):
        tree = forest[i][j]
        if tree > down:
            visible.add((i,j))
            down = tree

        scores[i][j] *= min(last[tree:]) - i
        last[tree] = i

p1 = len(visible)
p1 += 2*height + 2*width - 4

p2 = max(max(scores[i][j] for j in range(width)) for i in range(height))

if __name__=="__main__":
    print(f"Part1 : {p1}")
    print(f"Part2 : {p2}")