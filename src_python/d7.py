#!/usr/bin/env python3

class Dir():
    def __init__(self,parent,name,children):
        self.parent = parent
        self.name = name
        self.children = children
    
    def get_size():
        return sum(child.get_size() for child in children)
    
    def get_size
    
    def add_child(self,child):
        self.children[child.name] = child

class File():
    def __init__(self,parent,name,size):
        self.parent = parent
        self.name = name
        self.size = size

    def get_size():
        return size

curr_dir = None
Dir()
with open("../Input/d3.txt") as f:
    while (l := f.readline().strip()) != "":
        if l[2:4] == "cd":
            if l[5:] == "..":
                curr_dir = curr_dir.parent
            else:
                if (curr_dir := curr_dir.children.get()) == None:
                    exit(-1)
        if l[2:4] == "ls":
            (size_or_type,name) = f.readline().strip().split(" ")
            if size_or_type == "dir":
                child = Dir(curr_dir,name,{})
            else:
                child = File(curr_dir,name,int(size_or_type))
            curr_dir.add_child(child)

    # Input parsed



        

    
print(f"Part1 : {p1}")