import math

T = int(input())
for t in range(T):
    p, q = map(int,input().split())
    
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
            xpoints[0][0] = 0
        if len(xpoints) > 1:
            for i in range(1, len(xpoints)):
                if len(xpoints[i]) > 0 and len(xpoints[i-1]) > 0 and xpoints[i][2] == xpoints[i-1][2]:
                    if xpoints[i][2] == 'E':
                        xpoints[i-1] = []
                    else:
                        xpoints[i] = []
            xp = []
            for i in range(len(xpoints)):
                if len(xpoints[i]):
                    xp.append(xpoints[i])
            xpoints = xp

            if len(xpoints)%2 == 1:
                if xpoints[0][2] == 'E':
                    maxpeople = xpoints[0][1] + xpoints[1][1]
                    x = xpoints[0][0]
                    for i in range(2, len(xpoints)-1, 2):
                        people = xpoints[i][1] + xpoints[i+1][1]
                        if people > maxpeople:
                            maxpeople = people
                            x = xpoints[i][0]
                    if xpoints[-1][1] > maxpeople:
                        x = xpoints[-1][0]
                else:
                    maxpeople = xpoints[0][1]
                    x = xpoints[0][0]
                    for i in range(1, len(xpoints)-1, 2):
                        people = xpoints[i][1] + xpoints[i+1][1]
                        if people > maxpeople:
                            maxpeople = people
                            x = xpoints[i][0]
            else:
                if xpoints[0][2] == 'E':
                    maxpeople = 0
                    for i in range(0, len(xpoints)-1, 2):
                        people = xpoints[i][1] + xpoints[i+1][1]
                        if people > maxpeople:
                            maxpeople = people
                            x = xpoints[i][0]
                else:
                    maxpeople = xpoints[0][1]
                    x = xpoints[0][0]
                    for i in range(1, len(xpoints)-2, 2):
                        people = xpoints[i][1] + xpoints[i+1][1]
                        if people > maxpeople:
                            maxpeople = people
                            x = xpoints[i][0]
        else:
            x = xpoints[0][0]

    ###########################################################
    if len(ypoints) == 0:
        y = 0
    else:
        if ypoints[0][2] == 'S':
            ypoints[0][0] = 0
        if len(ypoints) > 1:
            for i in range(1, len(ypoints)):
                if len(ypoints[i]) > 0 and len(ypoints[i-1]) > 0 and ypoints[i][2] == ypoints[i-1][2]:
                    if ypoints[i][2] == 'N':
                        ypoints[i-1] = []
                    else:
                        ypoints[i] = []
            yp = []
            for i in range(len(ypoints)):
                if len(ypoints[i]):
                    yp.append(ypoints[i])
            ypoints = yp

            if len(ypoints)%2 == 1:
                if ypoints[0][2] == 'N':
                    maxpeople = ypoints[0][1] + ypoints[1][1]
                    y = ypoints[0][0]
                    for i in range(2, len(ypoints)-1, 2):
                        people = ypoints[i][1] + ypoints[i+1][1]
                        if people > maxpeople:
                            maxpeople = people
                            y = ypoints[i][0]
                    if ypoints[-1][1] > maxpeople:
                        y = ypoints[-1][0]
                else:
                    maxpeople = ypoints[0][1]
                    y = ypoints[0][0]
                    for i in range(1, len(ypoints)-1, 2):
                        people = ypoints[i][1] + ypoints[i+1][1]
                        if people > maxpeople:
                            maxpeople = people
                            y = ypoints[i][0]
            else:
                if ypoints[0][2] == 'N':
                    maxpeople = 0
                    for i in range(0, len(ypoints)-1, 2):
                        people = ypoints[i][1] + ypoints[i+1][1]
                        if people > maxpeople:
                            maxpeople = people
                            y = ypoints[i][0]
                else:
                    maxpeople = ypoints[0][1]
                    y = ypoints[0][0]
                    for i in range(1, len(ypoints)-2, 2):
                        people = ypoints[i][1] + ypoints[i+1][1]
                        if people > maxpeople:
                            maxpeople = people
                            y = ypoints[i][0]
        else:
            y = ypoints[0][0]
    
        
    print("Case #"+str(t+1)+":",x , y)
    
