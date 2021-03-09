T = int(input())
for t in range(T):
    s, k = input().split()
    k = int(k)
    s = list(s)
    flips = 0
   
    for i in range (len(s)-k+1):
        if (s[i] == '-'):
            s[i] = '+'
            flips = flips + 1
            
            for j in range (i+1, i+k):
                if (s[j] == '+'):
                    s[j] = '-'
                else:
                    s[j] = '+'
      

    for i in range (len(s)-1, len(s)-k, -1):
        if (s[i] == '-'):
            flips = 'IMPOSSIBLE'
            break

    print("Case #"+str(t+1)+":",flips)
