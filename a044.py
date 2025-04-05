while True:
    try:
        num = int(input())

        aa = num*num*num + 5*num+6

        bb = aa//6

        print(bb)
        

        
    except EOFError:
        break
