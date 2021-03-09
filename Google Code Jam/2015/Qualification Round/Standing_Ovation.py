T = int(input())
for t in range(T):
    n, s = input().split()
    n = int(n)
    friends = 0
    standing = int(s[0])

    for i in range(1, n+1):
        if (i > standing):
            friends = friends + i - standing
            standing = standing + i - standing
        standing = standing + int(s[i])

    print("Case #"+str(t+1)+":",friends)
