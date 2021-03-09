T = int(input())
for t in range(T):
    c, f, x = map(float,input().split())
    farms = 0
    time = 0
    rate = 2.0
    
    curMin = x/rate
    buy = x/(rate)

    while True:
        if curMin >= buy + x/(rate + f):
            time+=buy
            farms+=1
            rate = 2+f*farms
            curMin = time + x/rate
            buy = x/rate
        else:
            break
        
    print("Case #"+str(t+1)+":",curMin)
    
