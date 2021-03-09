import math

T = int(input())
for t in range(T):
    x, y, m = input().split()
    x = int(x)
    y = int(y)
    s = 'IMPOSSIBLE'

    manhattan = abs(x) + abs(y)
    if manhattan == 0:
        s = 0
    else:
        for i in range(len(m)):

            if m[i] == 'W':
                x -= 1 
            elif m[i] == 'E':
                x += 1
            elif m[i] == 'N':
                y += 1
            else:
                y -= 1

            manhattan = abs(x) + abs(y)
            
            if manhattan <= i+1:
                s = i+1
                break
        
    print("Case #"+str(t+1)+":",s)
    
