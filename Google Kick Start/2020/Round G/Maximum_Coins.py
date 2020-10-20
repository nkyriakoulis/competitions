T = input()
T = int(T)
for rep in range (0,T):
    N = input()
    N = int(N)
    sums = [0]*(2*(N-1)+1)

    S = []
    sum_mid = 0
    
    for i in range(0,N):
        S.append(input().split())
    
    for i in range(0,N):
        sum_up = 0
        sum_down = 0
        for j in range(0,i+1):
            sum_up = sum_up + int(S[j][(N-1)-i+j])
            sum_down = sum_down + int(S[(N-1)-i+j][j])
        sums[i] = sum_up
        sums[2*(N-1) - i] = sum_down
        sum_mid = sum_mid + int(S[i][i])

    sums[N-1] = sum_mid
    
    print ('Case #{}:'.format(rep+1),max(sums))
