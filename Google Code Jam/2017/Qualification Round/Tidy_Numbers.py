T = int(input())
for t in range(T):
    n = input()
    n = (list(n))
    

    for i in range(len(n)-1, 0, -1):
        if (int(n[i]) < int(n[i-1])):
            n[i] = '9'
            n[i-1] = str(int(n[i-1]) - 1)
            
            for j in range(i, len(n)):
                n[j] = '9'

    res = ''
    res = res.join(n)

    print("Case #"+str(t+1)+":",int(res))
