num = list(map(int,input().split()))

num.sort()

if num[0] + num[1] <= num[2]:
    print(num[0],num[1],num[2])
    print("No")
elif num[0]*num[0] + num[1]*num[1] < num[2]*num[2]:
    print(num[0],num[1],num[2])
    print("Obtuse")
elif num[0]*num[0] + num[1]*num[1] == num[2]*num[2]:
    print(num[0],num[1],num[2])
    print("Right")
elif num[0]*num[0] + num[1]*num[1] > num[2]*num[2]:
    print(num[0],num[1],num[2])
    print("Acute")
