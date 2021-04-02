T = int(input())
for t in range(T):

    r, c, h, v = map(int,input().split())
    grid = []
    chocos = 0
    s = 'POSSIBLE'
    customers = (h+1)*(v+1)

    for i in range(r):
        arr = input()
        for j in range(len(arr)):
            if arr[j] == '@':
                chocos += 1
        grid.append(list(arr))

    if chocos%(h+1) != 0 or chocos%(v+1) != 0:
        s = 'IMPOSSIBLE'
    else:
        ### HORIZONTAL CUTS ###
        hc = 0
        i = 0
        p = 0
        rcuts = []
        while hc < h and i < r:
            for j in range(len(grid[i])):
                if grid[i][j] == '@':
                    p += 1
            if p > chocos//(h+1):
                s = 'IMPOSSIBLE'
                break
            elif p == chocos//(h+1):
                hc += 1
                rcuts.append(i)
                p = 0
            i += 1

        if s != 'IMPOSSIBLE' and hc == h:
            p = 0
            for k in range(i, r):
                for j in range(len(grid[i])):
                    if grid[k][j] == '@':
                        p += 1
            if p != chocos//(h+1):
                s = 'IMPOSSIBLE'

        #### VERTICAL CUTS ###
        if s != 'IMPOSSIBLE':
            vc = 0
            i = 0
            p = 0
            vcuts = []
            while vc < v and i < c:
                for j in range(r):
                    if grid[j][i] == '@':
                        p += 1
                if p > chocos//(v+1):
                    s = 'IMPOSSIBLE'
                    break
                elif p == chocos//(v+1):
                    vc += 1
                    vcuts.append(i)
                    p = 0
                i += 1

            if s != 'IMPOSSIBLE' and vc == v:
                p = 0
                for k in range(i, c):
                    for j in range(r):
                        if grid[j][k] == '@':
                            p += 1
                if p != chocos//(v+1):
                    s = 'IMPOSSIBLE'


        ### CHECK EVERY SEGMENT ###
        if s != 'IMPOSSIBLE':
            each = chocos//customers
            # partition by horizontal cuts
            for i in range(len(rcuts)+1):
                if i == 0:
                    rprev = 0
                else:
                    rprev = rcuts[i-1]+1

                if i < len(rcuts):
                    rnext = rcuts[i]+1
                else:
                    rnext = len(grid)

                segr = grid[rprev:rnext]

                # partition by vertical cuts
                for j in range(len(vcuts) + 1):
                    if j == 0:
                        vprev = 0
                    else:
                        vprev = vcuts[j-1]+1

                    if j < len(vcuts):
                        vnext = vcuts[j]+1
                    else:
                        vnext = len(grid[0])

                    #check elements of segment
                    p = 0
                    for k in range(len(segr)):
                        for l in range(vprev, vnext):
                            if segr[k][l] == '@':
                                p += 1
                    if p != each:
                        s = 'IMPOSSIBLE'
                        break
                if s == 'IMPOSSIBLE':
                    break
                        
            
    
    
    print ('Case #{}:'.format(t+1), s)
    
