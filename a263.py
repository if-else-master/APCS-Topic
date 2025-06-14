from datetime import date

while True:
    try:
        a1,b1,c1 = map(int,input().split())
        a2,b2,c2 = map(int,input().split())

        date1 = date(a1,b1,c1)
        date2 = date(a2,b2,c2)

        dal = date1-date2

        print(abs(dal.days))
    except:
        break

