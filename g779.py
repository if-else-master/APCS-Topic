a,b = map(int,input().split())


if a % b == 0:
    print("YES")
elif str(b) in str(a):
    print("YES")
else:
    print("NO")
