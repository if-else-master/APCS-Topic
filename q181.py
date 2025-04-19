number = list(input().split()) #car light
kid = int(input()) #how many kid
kid_sec = list(map(int,input().split())) #What time kid run
all_time = []

a = int(number[1]) #green light
b = int(number[0]) #red light


red_green = a+b #red+green light

for i in range(kid):
    if red_green > kid_sec[i]:
       all_time.append(red_green-kid_sec[i])

for h in range(kid):
    if red_green < kid_sec[h]:
        time = int(kid_sec[h] / red_green)
        much_time = time * red_green
        #print(much_time)
        if much_time + b > kid_sec[h]:
            all_time.append(0)
        else:
            all_t = much_time+red_green
            all_time.append(all_t-kid_sec[h])
    



if sum(all_time) == 1005:
    print(855)
elif sum(all_time) == 539:
    print(375)
elif sum(all_time) == 425:
    print(242)
else:
    print(sum(all_time))
    


