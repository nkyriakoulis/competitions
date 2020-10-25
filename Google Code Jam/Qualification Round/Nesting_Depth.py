T = input()
T = int(T)
for rep in range (0,T):
    S = input()
    S1 = ""
    t=0
    prev = 0
    flag = 0
    for i in range (0,len(S),t+1):
        if (i>0):
            if (S[i-1] == 0):
                flag = 0
            if (S[i] > S[i-1]):
                flag = 1
            elif (S[i] < S[i-1]):
                flag = 2
            else :
                flag = 3
        if (int(S[i]) == 0): # If element is zero
            for m in range (prev):
                S1 = S1 + ")"
            S1 = S1 + S[i]
            flag = 0
            t = 0
        else: # Αν το στοιχείο δεν είναι 0
            if (flag == 0): # If the preceding element is 0 or this is the first element
                for j in range (int(S[i])):
                    S1 = S1 + "("
                S1 = S1 + S[i]
                t = 0
            elif (flag == 1): # If the preceding element is smaller
                for j in range (int(S[i])-int(S[i-1])):
                    S1 = S1 + "("
                S1 = S1 + S[i]
                t = 0
            elif (flag == 2): # If the preceding element is greater
                for j in range (int(S[i-1])-int(S[i])):
                    S1 = S1 + ")"
                S1 = S1 + S[i]
                t = 0
            else : #Αν πριν έχει ίσο στοιχείο
                S1 = S1 + S[i]
                t = t+1
                
        prev = int(S[i])

    if (S[i] !=0):
        for i in range (int(S[i])):
            S1 = S1 + ")"
            

    print ('Case #{}:'.format(rep+1), S1)
