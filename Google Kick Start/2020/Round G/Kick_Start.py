T = input()
T = int(T)
for rep in range (0,T):
    S = input()
    kicks = 0
    kickstarts = 0
    for i in range (0,len(S)-4):
        if (S[i:i+4] == 'KICK'):
            kicks = kicks + 1
        elif (S[i:i+5] == 'START'):
            kickstarts = kickstarts + kicks
    
    print ('Case #{}:'.format(rep+1),kickstarts)
