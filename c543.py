num = int(input())

ans = 0
int_list = []
str_list = []

while num >= 1:
    num = num-1
    num_list = list(str(num))
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])

    if sorted(num_list) == num_list:
        ans+=1
    
print(ans)
    

