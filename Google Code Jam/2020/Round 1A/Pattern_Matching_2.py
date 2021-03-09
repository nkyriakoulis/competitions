T = int(input())
for t in range(T):
    N = int(input())
    arr = [0]*N
    maxlengthend = 0
    maxindexend = -1
    maxlengthstart = 0
    maxindexstart = -1
    tmp = 0
    
    for i in range(N):
        arr[i] = input()
        for j in range(len(arr[i])):
            if arr[i][j] == '*':
                tmp = j
                break
        
        if len(arr[i][0:tmp]) > maxlengthstart:
            maxlengthstart = len(arr[i][0:tmp])
            maxindexstart = i
        if len(arr[i][tmp+1:]) > maxlengthend:
            maxlengthend = len(arr[i][tmp+1:])
            maxindexend = i
            
    word = arr[maxindexstart][0:maxlengthstart] + arr[maxindexend][len(arr[maxindexend]) - maxlengthend:]
    flag = 0
    
    for i in range(N):
        for j in range(len(arr[i])):
            if arr[i][j] == '*':
                tmp = j
                break
        l = len(arr[i])-tmp-1
        #chack for ending
        if arr[i][tmp+1:] != arr[maxindexend][-l:] and arr[i][tmp+1:] != '':
            flag = 1
            break
        #check for beginning
        if arr[i][:tmp] != arr[maxindexstart][:tmp] and arr[i][:tmp] != '':
            flag = 1
            break
        
    if flag == 1:
        word = '*'
    
    print ('Case #{}:'.format(t+1), word)
    
    
