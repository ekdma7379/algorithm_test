import sys

n = int(sys.stdin.readline())

dp = [0]

dp.extend(list(map(int, sys.stdin.readline().split())))

for i in range(2,n+1):
    for j in range(1,i//2+1):
        if dp[i] < dp[j] + dp[i-j]:
            dp[i] = dp[j] + dp[i-j]

print(dp[n])