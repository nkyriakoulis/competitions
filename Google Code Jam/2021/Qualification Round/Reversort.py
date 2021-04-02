T = int(input())
for rep in range(T):
    n = int(input())
    A = [int(y) for y in input().split()]
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
        


    print ('Case #{}:'.format(rep+1),cost)
