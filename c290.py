num = int(input())

list_num = list(str(num))
list_numt = []

for i in range(len(list_num)):
    list_numt.append(int(list_num[i]))

  

def q(list_numt,aa=[],bb=[]):

    for j in range(0,len(list_numt),2):
        aa.append(list_numt[j])        

    for k in range(1,len(list_numt),2):
        bb.append(list_numt[k])

    return aa, bb


o, t = q(list_numt)

if sum(t) - sum(o) < 0:
    print(-(sum(t)-sum(o)))
else:
    print(sum(t)-sum(o))
