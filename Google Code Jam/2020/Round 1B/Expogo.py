import math

T = int(input())
for t in range(T):
    x1, y1 = map(int,input().split())
    s = ''
    
    if x1%2 == y1%2:
        s = 'IMPOSSIBLE'
    else:
        x = abs(x1)
        y = abs(y1)
        limit = math.floor(math.log2(x+y))

        for i in range(limit, -1, -1):
            n = pow(2,i)
            #print(x,y)
            if abs(x) > abs(y):
                if x > 0:
                    x = x - n
                    s = 'E' + s
                else:
                    x = x + n
                    s = 'W' + s
            else:
                if y > 0:
                    y = y - n
                    s = 'N' + s
                else:
                    y = y + n
                    s = 'S' + s
            #print(x,y)
      
        s = list(s)
        if x1 < 0:
            for i in range(len(s)):
                if s[i] == 'E':
                    s[i] = 'W'
                elif s[i] == 'W':
                    s[i] = 'E'

        if y1 < 0:
            for i in range(len(s)):
                if s[i] == 'S':
                    s[i] = 'N'
                elif s[i] == 'N':
                    s[i] = 'S'

        s = ''.join(s)

        
    print("Case #"+str(t+1)+":",s)
    
