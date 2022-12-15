p1=0
p2=0
with open("d12.txt") as f:
    nodes = []
    for i,line in enumerate(f):
        node_line=[]
        for j,c in enumerate(line.strip()):
            if c=='S':
                start = (i,j)
                c='a'
            elif c=='E':
                end = (i,j)
                c='z'
                
            node_line.append(ord(c)-ord('a'))
                
            
        nodes.append(node_line)
    
#dijkstra
def dijkstra(graph,rel,start):
    #define adjacency matrix
    adjacency_matrix=[]
    dirs=((0,1),(0,-1),(1,0),(-1,0))
    for i,l in enumerate(nodes):
        k=[]
        for j in range(len(l)):
            edges=[(i+di,j+dj) for di,dj in dirs if 0<=i+di<len(nodes) and 0<=j+dj<len(l) and rel(nodes[i+di][j+dj],l[j])]
            
            k.append(edges)
            
        adjacency_matrix.append(k)
    
    #start dijkstra
    predecessors={}
    distances={}
    distances[start] = 0
    not_visited=set((i,j) for i in range(len(graph)) for j in range(len(graph[i])))
    while not_visited:
        #choose next node
        current_node = min(not_visited,key=lambda p: distances.get(p,1e9))
        
        #update distances
        for node in adjacency_matrix[current_node[0]][current_node[1]]:
            #if node == (40,21):
                #print("predecessor:", current_node, distances(current_node)
            if distances.get(node, 1e9) > distances.get(current_node,1e9)+1:
                distances[node]=distances[current_node]+1
                predecessors[node]=current_node
        
        not_visited.remove(current_node)
    
    return distances,predecessors

distances,_ = dijkstra(nodes,lambda i,j: i>=j-1,end)

p1=distances[start]
p2 = min(distances[(i,j)] for i,j in distances.keys() if nodes[i][j] == 0)

print(distances[start])
if __name__ == "__main__":
    print(f"Part1: {p1}")
    print(f"Part2: {p2}")