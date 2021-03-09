T = int(input())
for t in range(T):
    N = int(input())
    arr = [0]*N
    maxlength = 0
    maxindex = -1
    
    for i in range(N):
        arr[i] = input()
        if len(arr[i]) > maxlength:
            maxlength = len(arr[i])
            maxindex = i
            
    word = arr[maxindex][1:]
    flag = 0
    
    for i in range(N):
        l = len(arr[i])-1
        if arr[i][1:] != arr[maxindex][maxlength-l:]:
            flag = 1
            break
        
    if flag == 1:
        word = '*'
    
    print ('Case #{}:'.format(t+1), word)
    
