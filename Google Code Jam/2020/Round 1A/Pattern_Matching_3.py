T = int(input())
for t in range(T):
    N = int(input())
    arr = [[0]*3 for i in range(N)]
    maxlengthend = 0
    maxindexend = -1
    maxlengthstart = 0
    maxindexstart = -1
    tmp = 0
    
    for i in range(N):
        arr[i][0] = input()
        for j in range(len(arr[i][0])):
            if arr[i][0][j] == '*':
                arr[i][1] = j
                tmp = j
                break
        
        if len(arr[i][0][:tmp]) > maxlengthstart:
            maxlengthstart = len(arr[i][0][:tmp])
            maxindexstart = i
            
        for j in range(len(arr[i][0])-1,-1,-1):
            if arr[i][0][j] == '*':
                arr[i][2] = j
                tmp = j
                break
        if len(arr[i][0][tmp+1:]) > maxlengthend:
            maxlengthend = len(arr[i][0][tmp+1:])
            maxindexend = i
       
    start = arr[maxindexstart][0][0:maxlengthstart]
    end = arr[maxindexend][0][arr[maxindexend][2]+1:]
    mid = ''
    flag = 0
    
    for i in range(N):
        #check for beginning
        if arr[i][0][:arr[i][1]] != arr[maxindexstart][0][:arr[i][1]] and arr[i][0][:arr[i][1]] != '':
            flag = 1
            break
        #check for ending
        l = len(arr[i][0])-arr[i][2]-1
        if arr[i][0][arr[i][2]+1:] != arr[maxindexend][0][-l:] and arr[i][0][arr[i][2]+1:] != '':
            flag = 1
            break
        for j in range(arr[i][1]+1, arr[i][2]):
            if arr[i][0][j] != '*':
                mid += arr[i][0][j]
        
        
    if flag == 1:
        word = '*'
    else:
        word = start + mid + end
    
    print ('Case #{}:'.format(t+1), word)
    
    
