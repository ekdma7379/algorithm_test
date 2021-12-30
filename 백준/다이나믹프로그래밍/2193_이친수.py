import sys
MAX = 90
dp = [[0 for _ in range(2)] for _ in range(MAX+1)]

n = int(sys.stdin.readline())

if n < 3:
    print("1")
else:
    dp[2][0] = 1
    for i in range(3,MAX+1):
        dp[i][0] = sum(dp[i-1])
        dp[i][1] = dp[i-1][0]
    print(sum(dp[n]))