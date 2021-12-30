import sys

MAX = 100000
MOD = 1000000009
dp = [[0 for _ in range(4)] for _ in range(MAX+1)]

dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, MAX+1):
    dp[i][1] = dp[i-1][2] + dp[i-1][3]
    dp[i][2] = dp[i-2][1] + dp[i-2][3]
    dp[i][3] = dp[i-3][1] + dp[i-3][2]
    dp[i][1] %= MOD
    dp[i][2] %= MOD
    dp[i][3] %= MOD
n = int(sys.stdin.readline())
for _ in range(n):
    goal = int(sys.stdin.readline())
    print(sum(dp[goal])%MOD)
