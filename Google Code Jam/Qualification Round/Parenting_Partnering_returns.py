T = input()
T = int(T)
for rep in range (0,T):
    N = input()
    N = int(N)
    A = []
    
    for i in range (0,N):
        A.append([int(y) for y in input().split()])

    a = sorted(range(N), key=A.__getitem__)
    A = sorted(A)
    
    C = [A[0]]
    J = []
    S = [0]*(N)
    S[a[0]] = 'C'
    for i in range (1,N):
        if (len(J) > 0):
            if (C[len(C)-1][1] <= J[len(J)-1][1]):
                if (A[i][0]>=C[len(C)-1][1]):
                    C.append(A[i])
                    S[a[i]] = 'C'
                else:
                    S = 'IMPOSSIBLE'
                    break
            else:
                if (A[i][0]>=J[len(J)-1][1]):
                    J.append(A[i])
                    S[a[i]] = 'J'
                else:
                    S = 'IMPOSSIBLE'
                    break
        else:
            if (A[i][0]>=C[len(C)-1][1]):
                C.append(A[i])
                S[a[i]] = 'C'
            else:
                J.append(A[i])
                S[a[i]] = 'J'
    new = ""
    for x in S:
        new +=x

    
    print ('Case #{}:'.format(rep+1), new)
