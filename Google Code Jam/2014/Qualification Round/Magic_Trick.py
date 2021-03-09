T = int(input())
for t in range(T):
    ans1 = int(input())
    ar1 = [[0]*4]*4
    ar2 = [[0]*4]*4

    for i in range(4):
        ar1[i] = list(map(int,input().split()))

    ans2 = int(input())
    for i in range(4):
        ar2[i] = list(map(int,input().split()))

    count = 0
    for i in range(4):
        for j in range(4):
            if ar1[ans1-1][i] == ar2[ans2-1][j]:
                count+=1
                y = ar1[ans1-1][i]
    if count == 0:
        y = 'Volunteer cheated!'
    elif count > 1:
        y = 'Bad magician!'

    print("Case #"+str(t+1)+":",y)
   
                
