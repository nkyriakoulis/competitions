def checkCost(n, A):
    cost = 0

    for i in range(n-1):
        j = A.index(min(A[i:]))
        step = j - i + 1
        cost += step

        part1 = A[:i]
        part2 = A[i:j+1]
        part2.reverse()
        part3 = A[j+1:]
        
        A = part1 + part2 + part3

    return cost



T = int(input())
for rep in range(T):
    n, c = list(map(int,input().split()))
    cost = 0
    swaps = 0
    start = 0
    end = n - 1

    if n - 1 > c or c >= n*(n+1)/2:
        A = 'IMPOSSIBLE'
    else:
        A = []
        B = [0]*n
        for i in range(1, n+1):
            A.append(i)
            
        ##############################
        for i in range(0, n):
            if len(A) == 0:
                break
            j = A.index(min(A))
            
            step = len(A)
            if cost + step + n-(i+2) <= c:
                cost += step
                A.reverse()
                
                swaps += 1
                if swaps%2 == 1:
                    B[end] = i + 1
                    end -= 1
                    A = A[:len(A)-1]
                else:
                    B[start] = i + 1
                    start += 1
                    A = A[1:]
            else:
                cost += 1
                if swaps%2 == 1:
                    B[end] = i + 1
                    end -= 1
                    A = A[:len(A)-1]
                else:
                    B[start] = i + 1
                    start += 1
                    A = A[1:]
                
        for k in range(len(A)):
            B[start] = A[k]
            start += 1
        
        estimate = checkCost(n, B)
        if estimate == c:
            cost = c
                
            
    
    if cost != c:
        A = 'IMPOSSIBLE'
    else:
        A = " ".join(map(str, B))
        
        


    print ('Case #{}:'.format(rep+1),A)

