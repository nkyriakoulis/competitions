import math

T = int(input())
for t in range(T):
    n = int(input())
    m = [0]*n
    s = ''

    for i in range(n):
        m[i] = input()
        while len(m[i]) < 500:
            m[i] += m[i]
        m[i] = m[i][:500]
        m[i] = list(m[i])

    for i in range(500):
        a = {'R': 0, 'P': 0, 'S': 0}
        for j in range(n):
            if m[j][i] != '_':
                a[m[j][i]] += 1

        if a['R'] > 0 and a['P'] > 0 and a['S'] > 0:
            s = 'IMPOSSIBLE'
            break
        elif a['R'] == 0 and a['P'] == 0 and a['S'] == 0:
            break
        elif a['R'] >= 0 and a['S'] > 0 and a['P'] == 0:
            s += 'R'
            for j in range(n):
                if m[j][i] == 'S':
                    for k in range(i, len(m[j])):
                        m[j][k] = '_'
        elif a['R'] > 0 and a['P'] >= 0 and a['S'] == 0:
            s += 'P'
            for j in range(n):
                if m[j][i] == 'R':
                    for k in range(i, len(m[j])):
                        m[j][k] = '_'
        elif a['S'] >= 0 and a['P'] > 0 and a['R'] == 0:
            s += 'S'
            for j in range(n):
                if m[j][i] == 'P':
                    for k in range(i, len(m[j])):
                        m[j][k] = '_'
        else:
            s = 'IMPOSSIBLE'
            break
        
    for i in range(n):
        if m[i][-1] != '_':
            s = 'IMPOSSIBLE'
            break
    
        
        
    print("Case #"+str(t+1)+":",s)
    
