try:
    num1 = input().split()

    int_num1 = int(num1[0])
    int_num2 = int(num1[1])
    int_long = []

    armstrong_list = []

    for i in range(int_num1, int_num2+1):
        n = 0
        str_num = str(i)
        num_long = len(str_num)  # 數字的長度
        
       
        

        one_num = list(str(i))  # 將數字拆解成 ['1', '2', '3']
        int_one = list(map(int,one_num))

        

        result = sum(x**num_long for x in int_one)
        aa = int(i)       
        if result == aa:
            #print(str_num)            
            armstrong_list.append(str_num);

    bb = list(map(int, armstrong_list))    
    if bb == []:
        print("none")
    print(*bb,sep=' ')
    
        

except Exception as e:
    print('發生錯誤:', e)
