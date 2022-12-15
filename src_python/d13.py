p1=0

def parse_array(l):
    n = []
    el = ""
    lvl = 0
    for c in l[1:-1]:
        if c=='[':
            lvl+=1
        elif c==']':
            lvl-=1
            
        if c == ',' and not lvl:
            if el:
                n.append(el)
                el=""
        else:
            el += c
    if el:
        n.append(el)
    return n

def compare(left,right):
    left_val = parse_array(left) if left[0] == '[' else int(left)
    right_val = parse_array(right) if right[0] == '[' else int(right)
    
    if type(left_val) == type(right_val) == int:
        return None if left_val==right_val else left_val<right_val
    elif type(left_val) != type(right_val):
        (left_val,right_val) = [val if type(val) == list else [str(val),] for val in (left_val,right_val)]
    try:
        for x,y in zip(left_val,right_val,strict=True):
            val = compare(x,y)
            if val != None:
                return val
    except:
        return len(left_val) < len(right_val)
    return None

packets=[]
with open("d13.txt") as f:
    i=1
    while True:
        l1= f.readline().strip()
        l2= f.readline().strip()
        packets +=[l1,l2]
        res = compare(l1,l2)
        #print(l1,l2,res)
        p1 += i*res
        
        if(f.readline()==""):
            break
        i+=1

def rank_packet(p0,l_p):
    return sum(compare(p,p0) for p in l_p) + 1
    
r1=rank_packet("[[2]]",packets)
r2=rank_packet("[[6]]",packets)+1 #need to add the [[2]] packet
p2=r1*r2
    
if __name__ == "__main__":
    print(f"Part1 : {p1}")
    print(f"Part2 : {p2}")