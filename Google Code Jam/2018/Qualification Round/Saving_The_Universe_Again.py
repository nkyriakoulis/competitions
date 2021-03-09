T=int(input())
for t in range(T):
    d, s = input().split()
    d = int(d)
    moves = 0
    power = 1
    damage = 0
    countS = 0

    for i in range (len(s)):
        if (s[i] == 'C'):
            power = power*2
        else:
            damage = damage + power
            countS = countS + 1

    if (countS > d):
        moves = 'IMPOSSIBLE'
    else:
        s = list(s)
        while (damage > d):
            powerNew = power
            for i in range (len(s)-1, 0, -1):
                if (s[i] == 'C'):
                    powerNew = powerNew/2
                if (s[i] == 'S' and s[i-1] == 'C'):
                    s[i], s[i-1] = s[i-1], s[i]
                    damage = damage - powerNew/2
                    moves = moves + 1
                    break
                    
         
    print("Case #"+str(t+1)+":",moves)
