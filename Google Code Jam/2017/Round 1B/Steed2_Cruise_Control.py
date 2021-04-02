import math

T = int(input())
for t in range(T):
    d, n = map(int,input().split())
    
    horses = []
    
    for i in range(n):
        k, s = map(int,input().split())

        horses.append([k, s, 0])

    horses.sort(key=lambda x: x[0])

    t0 = (d - horses[-1][0])/horses[-1][1]
    horses[-1][2] = t0
    tmax = t0
    
    for i in range(n-2, -1, -1):
        ttemp = (d - horses[i][0])/horses[i][1]

        if ttemp > horses[i+1][2]:
            tmax = ttemp
            horses[i][2] = ttemp
        else:
            horses[i][2] = horses[i+1][2]
    

    u = d/tmax
        
    print("Case #"+str(t+1)+":",u)
    
