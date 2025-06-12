num = int(input())
build = list(map(int,input().split()))

ans = []
t = []

def aa(num,build,big,i=0,temp=None,ans=None):
    if temp is None:
        temp = []
    if ans is None:
        ans = []
    #if i >= len(build):
     #   ans.append(temp or [])
      #  return ans
    if i >= num:
      ans.append(temp or [])
      return ans
    
    if big > build[i]:
        temp.append(build[i])
        return aa(num,build,build[i],i+1,temp,ans)
    else:
        ans.append(temp)
        temp = []     
        return aa(num,build,build[i],i+1,temp,ans)

    
bb = []    
dd = aa(num,build,build[1])

for i in range(len(dd)):
    bb.append(len(dd[i]))

print(max(bb)+1)
        
