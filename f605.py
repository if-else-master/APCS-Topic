a,b = map(int,input().split())

Ans1 = []
Ans2 = 0

for i in range(a):
    g = list(map(int,input().split()))
    if max(g) - min(g) >= b:
        Ans1.append(sum(g) / len(g))
        Ans2+=1

print(Ans2,int(sum(Ans1)))
