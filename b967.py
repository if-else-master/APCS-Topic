grape = {}

fam = int(input())

def tree(grape,node, temp=None, depth=0):
    if temp is None:
        temp = set()
    temp.add(node)
    
    far_code = node
    max_depth = depth

    for neigh in grape[node]:
        if neigh not in temp:
            next_node, next_depth = tree(grape,neigh,temp,depth+1)
            if next_depth > max_depth:
                far_code = next_node
                max_depth = next_depth
    return far_code, max_depth


for _ in range(fam-1):
    u, v = input().split()

    if u not in grape:
        grape[u] = []
    if v not in grape:
        grape[v] = []
    grape[u].append(v)
    grape[v].append(u)

#print(list(grape.keys())[1])

#由上往下計算深度
u, _ = tree(grape,list(grape.keys())[0])
_, din = tree(grape, u)
print(din)
