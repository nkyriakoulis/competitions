import math

T = int(input())
for t in range(T):
    s = input()
    s = list(s)
    digits = []

    # Zeros
    zcount = 0 
    for i in range(len(s)):
        if s[i] == 'Z':
            zcount += 1
            s[i] = '_'
    
    d = {'E': zcount, 'R': zcount, 'O': zcount}
    while d['E'] + d['R'] + d['O'] > 0:
        for i in range(0, len(s)):
            if s[i] == 'E':
                if d['E'] > 0:
                    s[i] = '_'
                    d['E'] -= 1
            elif s[i] == 'R':
                if d['R'] > 0:
                    s[i] = '_'
                    d['R'] -= 1
            elif s[i] == 'O':
                if d['O'] > 0:
                    s[i] = '_'
                    d['O'] -= 1

    digits += [0]*zcount


    # Twos
    wcount = 0 
    for i in range(len(s)):
        if s[i] == 'W':
            wcount += 1
            s[i] = '_'
    
    d = {'T': wcount, 'O': wcount}
    while d['T'] + d['O'] > 0:
        for i in range(0, len(s)):
            if s[i] == 'T':
                if d['T'] > 0:
                    s[i] = '_'
                    d['T'] -= 1
            elif s[i] == 'O':
                if d['O'] > 0:
                    s[i] = '_'
                    d['O'] -= 1

    digits += [2]*wcount

    # Sixes
    xcount = 0 
    for i in range(len(s)):
        if s[i] == 'X':
            xcount += 1
            s[i] = '_'
    
    d = {'S': xcount, 'I': xcount}
    while d['S'] + d['I'] > 0:
        for i in range(0, len(s)):
            if s[i] == 'S':
                if d['S'] > 0:
                    s[i] = '_'
                    d['S'] -= 1
            elif s[i] == 'I':
                if d['I'] > 0:
                    s[i] = '_'
                    d['I'] -= 1

    digits += [6]*xcount

    # Eights
    gcount = 0 
    for i in range(len(s)):
        if s[i] == 'G':
            gcount += 1
            s[i] = '_'
    
    d = {'E': gcount, 'I': gcount, 'H': gcount, 'T': gcount}
    while d['E'] + d['I'] + d['H'] + d['T'] > 0:
        for i in range(0, len(s)):
            if s[i] == 'E':
                if d['E'] > 0:
                    s[i] = '_'
                    d['E'] -= 1
            elif s[i] == 'I':
                if d['I'] > 0:
                    s[i] = '_'
                    d['I'] -= 1
            elif s[i] == 'H':
                if d['H'] > 0:
                    s[i] = '_'
                    d['H'] -= 1
            elif s[i] == 'T':
                if d['T'] > 0:
                    s[i] = '_'
                    d['T'] -= 1

    digits += [8]*gcount

    # Fours
    ucount = 0 
    for i in range(len(s)):
        if s[i] == 'U':
            ucount += 1
            s[i] = '_'
    
    d = {'F': ucount, 'O': ucount, 'R': ucount}
    while d['F'] + d['O'] + d['R'] > 0:
        for i in range(0, len(s)):
            if s[i] == 'F':
                if d['F'] > 0:
                    s[i] = '_'
                    d['F'] -= 1
            elif s[i] == 'O':
                if d['O'] > 0:
                    s[i] = '_'
                    d['O'] -= 1
            elif s[i] == 'R':
                if d['R'] > 0:
                    s[i] = '_'
                    d['R'] -= 1

    digits += [4]*ucount

    # Fives
    fcount = 0 
    for i in range(len(s)):
        if s[i] == 'F':
            fcount += 1
            s[i] = '_'
    
    d = {'I': fcount, 'V': fcount, 'E': fcount}
    while d['I'] + d['V'] + d['E'] > 0:
        for i in range(0, len(s)):
            if s[i] == 'I':
                if d['I'] > 0:
                    s[i] = '_'
                    d['I'] -= 1
            elif s[i] == 'V':
                if d['V'] > 0:
                    s[i] = '_'
                    d['V'] -= 1
            elif s[i] == 'E':
                if d['E'] > 0:
                    s[i] = '_'
                    d['E'] -= 1

    digits += [5]*fcount

    # Sevens
    vcount = 0 
    for i in range(len(s)):
        if s[i] == 'V':
            vcount += 1
            s[i] = '_'
    
    d = {'S': vcount, 'N': vcount, 'E': 2*vcount}
    while d['S'] + d['N'] + d['E'] > 0:
        for i in range(0, len(s)):
            if s[i] == 'S':
                if d['S'] > 0:
                    s[i] = '_'
                    d['S'] -= 1
            elif s[i] == 'N':
                if d['N'] > 0:
                    s[i] = '_'
                    d['N'] -= 1
            elif s[i] == 'E':
                if d['E'] > 0:
                    s[i] = '_'
                    d['E'] -= 1

    digits += [7]*vcount

    # Ones
    ocount = 0 
    for i in range(len(s)):
        if s[i] == 'O':
            ocount += 1
            s[i] = '_'
    
    d = {'N': ocount, 'E': ocount}
    while d['N'] + d['E'] > 0:
        for i in range(0, len(s)):
            if s[i] == 'N':
                if d['N'] > 0:
                    s[i] = '_'
                    d['N'] -= 1
            elif s[i] == 'E':
                if d['E'] > 0:
                    s[i] = '_'
                    d['E'] -= 1

    digits += [1]*ocount

    # Nines
    ncount = 0 
    for i in range(len(s)):
        if s[i] == 'N':
            ncount += 1
            s[i] = '_'
    ncount = ncount//2
    
    d = {'I': ncount, 'E': ncount}
    while d['I'] + d['E'] > 0:
        for i in range(0, len(s)):
            if s[i] == 'I':
                if d['I'] > 0:
                    s[i] = '_'
                    d['I'] -= 1
            elif s[i] == 'E':
                if d['E'] > 0:
                    s[i] = '_'
                    d['E'] -= 1

    digits += [9]*ncount

    #Threes
    threecount = 0
    for i in range(0, len(s)):
        if s[i] != '_':
            threecount +=1

    threecount = threecount//5
    digits += [3]*threecount

    #Get number
    digits.sort()
    digits = [str(digit) for digit in digits]
    
    
        
    print("Case #"+str(t+1)+":",''.join(digits))
    
