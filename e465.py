M,S,N = map(int,input().split())

box = list(map(int,input().split()))

temp = []

a = 0

for i in range(N):
    a = a+box[i]
    for j in range(i,N-1):
        a = a+box[j+1]
        temp.append(a)
        temp.append(box[i]+box[j+1])
    a = 0

cho = min(temp, key=lambda x: abs(x-S))
print(cho)
