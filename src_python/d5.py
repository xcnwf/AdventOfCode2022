#!/usr/bin/env python3
p1 = 0
p2 = 0
with open("../Inputs/d5.txt") as f:
    line = f.readline()
    nb_col = ((len(line) - 3) // 4) + 1
    cols = [[] for _ in range(nb_col)]
    while(True):
        if line.startswith(" 1"):
            break
        for i in range(nb_col):
            if ((el := line[1+4*i]) != " "):
                cols[i] += el
        line = f.readline()
    #skip empty line
    f.readline()

    cols2 = cols.copy()
    for l in f:
        (n,dep,arr) = (int(el) for el in l.split()[1::2])
        cols[arr-1] = list(reversed(cols[dep-1][:n])) + cols[arr-1]
        cols[dep-1] = cols[dep-1][n:]
        cols2[arr-1] = cols2[dep-1][:n] + cols2[arr-1]
        cols2[dep-1] = cols2[dep-1][n:]

p1 = ''.join(cols[i][0] for i in range(nb_col))
p2 = ''.join(cols2[i][0] for i in range(nb_col))

if __name__=="__main__":
    print(f"Part1 : {p1}")
    print(f"Part2 : {p2}")