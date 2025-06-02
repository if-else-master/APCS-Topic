M,N,k,r,c = map(int,input().split())
box_list = []
score = 0
ans = 0
for i in range(M):
    number = list(map(int,input().split()))
    box_list.append(number)
    
box_list[r][c] = box_list[r][c] - 1
ans+=1
score = score + box_list[r][c]

stop = 1

def right(r,c,ans,score,stop):
    i = 1
    c = c+1
    box_list[r][c] = box_list[r][c] -1
    ans+=1
    score = score + box_list[r][c]
    print(r,c)
    if box_list[r][c+1] == 0:
        stop-=1
    return ans


while stop != 0: 
    print(right(r,c,ans,score,stop))
    print(stop)
        
        
                    
 
