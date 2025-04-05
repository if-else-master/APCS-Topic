while True:
    try:
        num = int(input())
        aa = num+num

        print(aa)
        
    except EOFError:
        break
