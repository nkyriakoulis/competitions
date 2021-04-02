import math

T = int(input())
for t in range(T):
    n, k = map(int,input().split())
    
    p = []
    
    for i in range(n):
        r, h = map(int,input().split())
        side = 2*math.pi*r*h
        base = math.pi*pow(r, 2)
        
        p.append([r, h, side, base])

    p.sort(key=lambda x: x[0])

    maxarea = 0
    
    for i in range(k-1, n):
        base = p[i][3]

        part = p[:i]
        part.sort(key=lambda x: x[2])

        area = base + p[i][2]
        if k > 1:
            for j in range(i-1, i - k, -1):
                area += part[j][2]

        if area > maxarea:
            maxarea = area
    
    
        
    print("Case #"+str(t+1)+":",maxarea)
    
