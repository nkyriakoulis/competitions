T = input()
T = int(T)
for rep in range (0,T):
    N = input()
    N = int(N)
    L = input()
    path = ''

    for i in range (2*N - 2):
        if (L[i] == 'E'):
            path = path + 'S'
        else:
            path = path + 'E'


    print ('Case #{}:'.format(rep+1),path)
