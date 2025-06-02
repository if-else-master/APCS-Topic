num = int(input())

number = list(map(int,input().split()))
number.sort()

max_ans = 0
min_ans = 0

max_num = max(number)
min_num = min(number)

def wor(number):
    for j in number:
        print(j,end=' ')
    print()
    print(max(number))
    print("worst case")

def good(number):
    for j in number:
        print(j,end=' ')
    print()
    print("best case")
    print(min(number))

if max_num < 60:
    wor(number)
elif min_num >= 60:
    good(number)
else:
    # 中間有及格與不及格的人
    for i in range(num):
        if number[i] < 60 and number[i+1] >= 60:
            min_ans = number[i]
            max_ans = number[i+1]
            break  # 找到後就可以停止了

    for j in number:
        print(j, end=' ')
    print()
    print(min_ans)
    print(max_ans)

