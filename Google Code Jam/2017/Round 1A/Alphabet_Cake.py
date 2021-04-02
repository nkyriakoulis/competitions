T = int(input())
for t in range(T):
    r, c = map(int,input().split())
    grid = []

    for i in range(r):
        row = input()
        row = list(row)
        grid.append(row)

    for i in range(c):
        start = 0
        ccount = 0
        for j in range(r):
            if grid[j][i] != '?':
                ccount += 1
                for k in range(start, j+1):
                    grid[k][i] = grid[j][i]
                start = j+1
        if ccount != 0 and grid[r-1][i] == '?':
            for k in range(start, r):
                grid[k][i] = grid[start-1][i]
    
    start = 0
    found = False
    for i in range(c):
        if grid[0][i] == '?':
            if i == 0:
                pass
            else:
                for j in range(r):
                    grid[j][i] = grid[j][i-1]
                if grid[0][i] != '?':
                    found = True
        else:
            if found == False:
                for k in range(start, i):
                    for j in range(r):
                        grid[j][k] = grid[j][i]
                found = True

    
    print ('Case #{}:'.format(t+1))
    for i in range(r):
        print(''.join(grid[i]))
    
