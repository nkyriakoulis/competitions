T = input()
T = int(T)
for rep in range (0,T):
    N = input()
    N = int(N)
    A = []
    fact = 1
    sum = 0
    for i in range (0,N):
        A.append([int(y) for y in input().split()])
        fact = fact*(i+1)
        sum = sum+(i+1)
    
    k = 0
    r = 0
    c = 0

    for i in range (0,N):
        k = k + A[i][i]
        p1 = 1
        s1 = 0
        p2 = 1
        s2 = 0
        for j in range (0,N):
            p1 = p1*A[i][j]
            s1 = s1+A[i][j]
            
            p2 = p2*A[j][i]
            s2 = s2+A[j][i]
            
        if ((p1 != fact) or (s1 != sum)):
            r = r+1
            

        if ((p2 != fact) or (s2 != sum)):
            c = c+1
        

    print ('Case #{}:'.format(rep+1),k,r,c)
