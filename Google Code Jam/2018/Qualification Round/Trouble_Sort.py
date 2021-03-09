T = int(input())
for t in range (T):
    n = int(input())
    L = list(map(int,input().split()))
    ans = 'OK'

    odds = L[1::2]
    evens = L[::2]

    odds.sort()
    evens.sort()
    
    result = [None]*n
    result[::2] = evens
    result[1::2] = odds

    for i in range(n-1):
        if (result[i] > result[i+1]):
            ans = i
            break
    

    print("Case #"+str(t+1)+":",ans)

    
