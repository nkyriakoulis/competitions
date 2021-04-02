import string

T = int(input())
for rep in range(T):
    n = int(input())
    parties = []
    moves = []
    letters = string.ascii_uppercase
    
    for i in range(26):
        parties.append(letters[i])
        
    senators = list(map(int,input().split()))
    s = sum(senators)
    while s > 0:
        M = max(senators)
        indices = [i for i, j in enumerate(senators) if j == M]

        senators[indices[0]] -= 1
        M = max(senators)
        if M <= sum(senators)//2:
            moves.append(letters[indices[0]])
            s -= 1
        else:
            senators[indices[1]] -= 1
            s -= 2
            moves.append(letters[indices[0]]+letters[indices[1]])

    moves = " ".join(map(str, moves))
    
    print ('Case #{}:'.format(rep+1),moves)
