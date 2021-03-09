T = int(input())
for t in range(T):
    n = input()
    digits = [0]*10
    result = 'INSOMNIA'

    for i in range (10):
        digits[i] = str(i)

    if (int(n) == 0):
        True
    else:
        j = 1
        while (len(digits)):
            result = str(int(n)*j)
            for i in range(len(result)):
                if (result[i] in digits):
                    digits.remove(result[i])
            j = j + 1

    print("Case #"+str(t+1)+":",result)
