T = input()
T = int(T)
for rep in range (0,T):
    N = input()
    N = int(N)
    A = list(map(int, input().strip().split(' ')))
    if (N==1):
        print ('Case #{}:'.format(rep+1), 1)
    else:
        max = A[0]
        sum = 0
        
        if (A[0]>A[1]):
            sum = sum +1
        for i in range (1,N-1):
            if (A[i]>max):
                max = A[i]
                if (A[i]>A[i+1]):
                    sum = sum +1
        if (A[N-1]>max):
            sum = sum +1
    
        
        print ('Case #{}:'.format(rep+1), sum)
