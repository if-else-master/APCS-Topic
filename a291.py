Ans = list(map(int,input().split()))
num = int(input())

A = 0
B = 0
K = 0

for i in range(4):
    a = list(map(int,input().split()))
    if a[i] in Ans:
        if a[i] == Ans[i]:
            A+=1
        else:
            B+=1
    else:
        continue
    print(f"{A}A{B}B")
    A = 0
    B = 0
    
