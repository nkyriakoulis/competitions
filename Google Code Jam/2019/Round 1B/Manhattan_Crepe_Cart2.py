import math

T = int(input())
for t in range(T):
    p, q = map(int,input().split())
    #m = []
    east = []
    west = []
    north = []
    south = []
    
    for i in range(p):
        x, y, d = input().split()

        if d == 'E':
            east.append(int(x)+1)
        elif d == 'W':
            west.append(int(x)-1)
        elif d == 'N':
            north.append(int(y)+1)
        else:
            south.append(int(y)-1)
    
    
    east.sort()
    west.sort(reverse=True)
    north.sort()
    south.sort(reverse=True)
    
    east2 = []
    west2 = []
    north2 = []
    south2 = []

    if len(east) > 0:
        east2.append([east[0], 1, 'E'])

    if len(west) > 0:
        west2.append([west[0], 1, 'W'])

    if len(north) > 0:
        north2.append([north[0], 1, 'N'])

    if len(south) > 0:
        south2.append([south[0], 1, 'S'])
       
    
    for i in range(1, len(east)):
        if east[i] == east2[-1][0]:
            east2[-1][1] += 1
        else:
            east2.append([east[i], i+1, 'E'])

    for i in range(1, len(west)):
        if west[i] == west2[-1][0]:
            west2[-1][1] += 1
        else:
            west2.append([west[i], i+1, 'W'])

    for i in range(1, len(north)):
        if north[i] == north2[-1][0]:
            north2[-1][1] += 1
        else:
            north2.append([north[i], i+1, 'N'])

    for i in range(1, len(south)):
        if south[i] == south2[-1][0]:
            south2[-1][1] += 1
        else:
            south2.append([south[i], i+1, 'S'])

    xpoints = east2
    for i in range (len(west2)):
        xpoints.append(west2[i])
    

    ypoints = north2
    for i in range (len(south2)):
        ypoints.append(south2[i])
    
    xpoints.sort(key=lambda x:x[0])
    ypoints.sort(key=lambda x:x[0])

    if len(xpoints) == 0:
        x = 0
    else:
        if xpoints[0][2] == 'W':
            x = 0
        else:
            x = xpoints[0][0]
        maxpeople = xpoints[0][1]
        people = 0
        left = x
        for i in range(1, len(xpoints)):
            if xpoints[i][2] == 'W':
                if xpoints[i-1][2] != 'W':
                    people += xpoints[i][1]
            else:
                if xpoints[i-1][2] == 'W':
                    if people > maxpeople:
                        maxpeople = people
                        x = left
                people = xpoints[i][1]
                left = xpoints[i][0]
        if people > maxpeople:
            x = left
        

    if len(ypoints) == 0:
        y = 0
    else:
        if ypoints[0][2] == 'S':
            y = 0
        else:
            y = ypoints[0][0]
        maxpeople = ypoints[0][1]
        people = 0
        bottom = y
        for i in range(1, len(ypoints)):
            if ypoints[i][2] == 'S':
                if ypoints[i-1][2] != 'S':
                    people += ypoints[i][1]
            else:
                if ypoints[i-1][2] == 'S':
                    if people > maxpeople:
                        maxpeople = people
                        y = bottom
                people = ypoints[i][1]
                bottom = ypoints[i][0]
        if people > maxpeople:
            y = bottom
        
    print("Case #"+str(t+1)+":",x , y)
    
