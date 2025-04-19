red_time, green_time = map(int, input().split())
kid = int(input()) #how many kid
kid_sec = list(map(int,input().split())) #What time kid run
all_time = []

a = green_time
b = red_time


red_green = a+b #red+green light

for i in range(kid):
    if red_green > kid_sec[i]:
       all_time.append(red_green-kid_sec[i])
    else:
        time = int(kid_sec[i] / red_green)
        much_time = time * red_green
        #print(much_time)
        if much_time + b > kid_sec[i]:
            all_time.append(0)
        else:
            all_t = much_time+red_green
            all_time.append(all_t-kid_sec[i])
    
print(sum(all_time))
    


