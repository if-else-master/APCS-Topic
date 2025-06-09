a,b = map(int,input().split())


listo = list(map(int,input().split()))
listt = list(map(int,input().split()))




def sn(listo,listt,num=None):
    temp = []
    if num is None:
        for i in range(len(listo)):
            for j in range(len(listt)):
                temp.append(listo[i]*listt[j])

        num = max(temp)
        for i in range(len(listo)):
            for j in range(len(listt)):
                if listo[i]*listt[j] == num:           
                    listo.remove(max(listo))
                    listt.remove(max(listt))                   
                    return sn(listo,listt,num)
                    break
        
    for i in range(len(listo)):
        for j in range(len(listt)):
            if listo[i]*listt[j]+num > num:
                num = num+listo[i]*listt[j]                
                listo.remove(listo[i])
                listt.remove(listt[j])                
                return sn(listo,listt,num)
            else:
                continue
    return num
                
print(sn(listo,listt))
     
