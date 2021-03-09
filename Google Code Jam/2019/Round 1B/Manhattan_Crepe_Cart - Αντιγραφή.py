import math

T = int(input())
for t in range(T):
    p, q = map(int,input().split())
    mx = []
    my = []
    xpoints = [[0, 0]]
    ypoints = [[0, 0]]
    
    
    for i in range(p):
        x, y, d = input().split()
        
        if d == 'E' or d == 'W':
            mx.append([x, d])
            if d == 'E':
                xpoints.append([x+1, 0])
        else:
            my.append([y, d])
            if d == 'N':
                ypoints.append([y+1, 0])

    xpoints.sort(key=lambda x:x[0])
    ypoints.sort(key=lambda x:x[0])

    for i in range(len(mx)):
        if mx[i]
    

    #xmax = max(xpoints)
    #ymax = max(ypoints)

    #x = xpoints.index(xmax)
    #y = ypoints.index(ymax)
        
    print("Case #"+str(t+1)+":",x , y)
    
