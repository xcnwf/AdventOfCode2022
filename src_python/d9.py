p1=0
p2=0
with open("d9_full.txt") as f:
    for (i,l) in enumerate(f):
        j = l.find("H")+1
        if j>=0:
            break

    while(f.readline().startswith(".")): pass

    instr = [(l[0],int(l[2:-1])) for l in f.readlines()]

h_i,h_j=t_i,t_j=i,j
visited = set()

dirs = {'R':(0,1),'L':(0,-1),'U':(1,0),'D':(-1,0)}

for (dir,steps) in instr:
    for _ in range(steps):
        dx,dy = dirs[dir]
        new_h_i,new_h_j = h_i+dx,h_j+dy
        if abs(new_h_i-t_i) == 2 or abs(new_h_j-t_j) == 2:
            t_i,t_j = h_i,h_j
        h_i,h_j = new_h_i,new_h_j
        visited.add((t_i,t_j))
#print(visited)

p1 = len(visited)
if __name__== "__main__":
    print(f"Part1 : {p1}")
    print(f"Part2 : {p2}")
