nk = list(map(int,input().split()))
number = list(map(int, input().split()))

group = [number[i:i+nk[1]] for i in range(0,len(number),nk[1])]

print(group)
