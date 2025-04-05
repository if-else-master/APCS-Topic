while True:
    try:
        num = int(input())
        bb = num - 2
        aa = (num * num - bb)
        print(aa)
    except EOFError:
        break  # 沒有輸入就結束迴圈
