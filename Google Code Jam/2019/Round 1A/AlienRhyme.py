T = int(input())
for t in range(T):
    N = int(input())
    arr = [0]*N
    words = 0
    blacklist = []
    
    for i in range(N):
        arr[i] = input()

    for i in range(N-1):
        maxrhymelength = 0
        maxrhyme = ''
        
        for j in range(i+1, N):
            rhymelength = 0
            for k in range(min(len(arr[i]), len(arr[j]))):
                if arr[i][(-1)*k -1] == arr[j][(-1)*k -1]:
                    rhymelength += 1
                else:
                    break
            if rhymelength > maxrhymelength:
                maxrhymelength = rhymelength
                maxrhyme = arr[i][(-1)*maxrhymelength:]
                if maxrhyme not in blacklist:
                    blacklist.append(maxrhyme)
                    words += 2
                    arr[maxIndex] = ''
            
    
    
    print ('Case #{}:'.format(t+1), word)
    
