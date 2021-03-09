T = int(input())
for t in range(T):
    s = input()
    flips = 0

    if (s[0] == '-'):
        flips = 1
    prev = s[0]

    for i in range(1, len(s)):
        if (s[i] != prev):
            if (s[i] == '-'):
                flips = flips + 2
        prev = s[i]

    print("Case #"+str(t+1)+":",flips)
