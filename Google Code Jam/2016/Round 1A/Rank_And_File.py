T = int(input())
for t in range(T):
    n = int(input())
    d = {}
    r = []

    for i in range(2*n - 1):
        integers = [int(x) for x in input().split()]
        for elem in integers:
            if elem in d:
                d[elem] += 1
            else:
                d[elem] = 1

    for elem in d:
        if d[elem]%2 == 1:
            r.append(elem)

            if len(r) == n:
                break

    r.sort()
    
    print ('Case #{}:'.format(t+1), *r)
    
    
