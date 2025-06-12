n=int(input())
w1,w2,h1,h2=map(int,input().split())
drinks=list(map(int,input().split()))
high,ans=0,0#初始目前高度，答案為0
for item in drinks:
    if high<h1:#從第一杯裝
        up=min(item//(w1**2),h1-high)#如果裝入後超過第一杯高度，增加高度設為(第一杯高度減目前高度)
        item-=(up)*(w1**2)
        if item>0:up+=min(item//(w2**2),h2)#有剩的飲料，裝入第二杯。
    elif h1<=high<h1+h2:up=min(item//(w2**2),h1+h2-high)
    else:break#剩下為0，不必判斷
    ans=max(ans,up)
    high+=up
print(ans)
