import math

T = int(input())
for t in range(T):
    p, q = map(int,input().split())
    #m = []
    #xpoints = [0]*(q+1)
    #ypoints = [0]*(q+1)
    xsets = []
    ysets = []
    
    for i in range(p):
        x, y, d = input().split()
        #m.append([x, y, d])
        if d == 'E':
            xsets.append([x+1, q])
        elif d == 'W':
            xsets.append([0, x-1])
        elif d == 'N':
            ysets.append([y+1, q])
        else:
            ysets.append([0, y-1])
    

    
        
    print("Case #"+str(t+1)+":",x , y)
    
