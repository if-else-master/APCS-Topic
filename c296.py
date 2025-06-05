N,M,K = map(int,input().split())

game = []

for i in range(1,N+1):
    game.append(i)

#print(game)
    
def point(game,game,M,K=0,temp=None):   
    if temp is None:
        temp = []
    for n in range(len(temp)):
        game.append(temp[n])
    if K == 1:
        return game
    
    for j in range(0,len(game),M):
        temp.append(game[j])
        print(temp)
    print(K)
    return point(game,temp,M,K-1,temp)


point(game,game,M,K)


#1 2 3 4 5 1 2 3 4 5
