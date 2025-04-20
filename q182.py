#aa = "cba"
#print(''.join(sorted(aa)))
#aa = "abc"
#print(list(aa))

def zero(chrang):
    list_word = list(chrang)
    long = len(list_word)    
    for j in range(0,long-1,2):
        #list_word[j],list_word[j+1] = list_word[j+1],list_word[j]
        temp = list_word[j]
        list_word[j] = list_word[j+1]
        list_word[j+1] = temp
    return ''.join(list_word)

def one(chrang):
    temp = []
    temp2 = []
    list_word = list(chrang)
    long = len(list_word)
    for j in range(2,long+1,2):
        temp.append(list_word[j-2:j])

    for h in range(0,len(temp)):
        aa = ''.join(sorted(temp[h]))
        temp2.append(aa)
    return ''.join(temp2)


def two(chrang):
    temp = []
    temp2 = []
    ans = []
    list_word = list(chrang)
    long = len(list_word)
    aa = long/2
    temp.append(list_word[0:int(aa)])
    temp2.append(list_word[int(aa):long])

    for i in range(len(temp[0])):
        ans.append(temp[0][i])
        ans.append(temp2[0][i])
    return ''.join(ans)
            
    


word = input()
how_many = int(input())
part = []

for i in range(how_many):
     part.append(int(input()))


for h in range(how_many):
    if part[h] == 0:
        word = zero(word)
    elif part[h] == 1:
        word = one(word)
    elif part[h] == 2:
        word = two(word)

print(word)
    
