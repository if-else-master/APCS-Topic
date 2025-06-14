num = int(input())
b = {}
a = list(map(int,input().split()))

a.sort()
print(' '.join(map(str,a)))

print(' '.join(map(str,sorted(set(a), reverse=True))))
