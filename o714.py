n,m,p = input().split()

n = int(n)

up = list(map(int,input().split()))
down = list(map(int,input().split()))

dic = {}

for i in range(n):
    for j in range(n):
        value = []
        for k in range(up[i],down[i]+1):
            value.append(k)
        dic[i] = value
        
print(dic)

def trin(dic,n,m,first,go=0):
    temp = dic[go][-1]

    for i in range(go,n):
        if temp in dic[i+1] and temp != dic[i+1][-1]:
            aa = dic[i+1][-1]
            print(aa)
            return trin(dic,n,m,aa,go+1)
        else:
            continue
    

first = dic[0][-1]

#dic
#n m
#first

print(trin(dic,n,m,first))
