import sys

MAX = 100
MOD = 1000000000
dp = [[1 for _ in range(10)] for _ in range(MAX+1)]
n = int(sys.stdin.readline())
dp[1][0] = 0

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n])%MOD)




