N, K = map(int, input().split())
list_one = list(map(int, input().split()))
list_two = list(map(int, input().split()))
ans = []

for i in range(N):
    mic = []  
    for j in range(list_one[i], list_two[i] + 1):
        mic.append(j)
    ans.append(mic)        

print(ans)


for k in range(K):
    for j in range(len(ans[k])):
        if ans
    
