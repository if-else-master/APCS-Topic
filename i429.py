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
                    listo.remove(listo[i])
                    listt.remove(listt[j])                   
                    return sn(listo,listt,num)
                    break
    temp2 = []
    for k in range(len(listo)):
        for h in range(len(listt)):
            temp2.append(listo[k]*listt[h])
            
    if not temp2:
        return num  # 如果沒有可乘的對，直接回傳結果

    
    aa = max(temp2)
    if num+max(temp2) > num:
        for i in range(len(listo)):
            for j in range(len(listt)):
                if listo[i]*listt[j] == aa:
                    num = num+max(temp2)              
                    listo.remove(listo[i])
                    listt.remove(listt[j])                
                    return sn(listo,listt,num)
                else:
                    continue
    return num
                
print(sn(listo,listt))
     
