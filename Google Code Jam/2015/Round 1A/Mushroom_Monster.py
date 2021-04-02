import string

T = int(input())
for rep in range(T):
    n = int(input())
        
    m = list(map(int,input().split()))
    ways = [0, 0]
    maxdiff = 0

    for i in range(n-1):
        d = m[i] - m[i+1]
        if d > 0:
            ways[0] += d
        if d > maxdiff:
            maxdiff = d

    for i in range(n-1):
        if m[i] >= maxdiff:
            ways[1] += maxdiff
        else:
            ways[1] += m[i]

    moves = " ".join(map(str, ways))
    
    print ('Case #{}:'.format(rep+1),moves)

    
