T = input()
T = int(T)
for rep in range (0,T):
    N = input()
    x1 = ''
    x2 = ''
    
    for i in range(len(N)):
        if (N[i] == '4'):
            x1 = x1 + '2'
            x2 = x2 + '2'
        else :
            x1 = x1 + N[i]
            x2 = x2 + '0'
    


    print ('Case #{}:'.format(rep+1),x1,x2)
