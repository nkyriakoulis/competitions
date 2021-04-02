T = input()
T = int(T)
for rep in range (0,T):
    n, k = map(int,input().split())
    s = input()
    goodness = 0

    for i in range(n//2):
        if s[i] != s[n-i-1]:
            goodness += 1
            
    r = abs(k - goodness)

    print ('Case #{}:'.format(rep+1), r)
