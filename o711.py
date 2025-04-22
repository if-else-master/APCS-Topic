number = int(input())
w1, w2, h1, h2 = map(int,input().split())

water = list(map(int,input().split()))

ans = 0
aa = 0
max_num = []



for i in range(number):
    cm2_down = w1**2 * h1
    cm2_up = w2**2 * h2
    if cm2_down + cm2_up <= water[i]:
        ans = h1+h2
        max_num.append(int(ans))
    elif cm2_down + cm2_up > water[i]:
        if water[i] > cm2_down and i == 0:
            ans = (water[i] - cm2_down) / w2**2
            ans = ans+h1
            max_num.append(int(ans))
        elif water[i] <= cm2_down and i == 0:
            ans = water[i] / w1**2
            max_num.append(int(ans))        

        if i > 0:
            if max_num[i-1] > h1:
                aa = max_num[i-1] - h1
                cmp2_up = w2**2 * (h2-aa)            
                ans = (cmp2_up - water[i]) / w2 ** 2
                max_num.append(int(ans))            
            elif max_num[i-1] <= h1:
                aa = h1 - max_num[i-1]
                bb = w1**2 * aa
                dd = water[i] - bb
                ans = dd / w2**2
                max_num.append(int(ans))

print(max(max_num))
    
    
