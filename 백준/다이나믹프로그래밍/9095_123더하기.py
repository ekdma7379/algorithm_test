# 직관적인 아이디어로 구현

# import sys
# MAX = 10
# n = int(sys.stdin.readline())
# dp = [set() for _ in range(MAX+1)]
# dp[1].add("1")
# dp[2].add("2")
# dp[2].add("1+1")
# dp[3].add("3")
# dp[3].add("1+1+1")
# dp[3].add("1+2")
# dp[3].add("2+1")
# for i in range(4,MAX+1):
#     for sen in dp[i-1]:
#         dp[i].add("1+"+sen)
#         dp[i].add(sen+"+1")
#     for sen in dp[i-2]:
#         dp[i].add("2+"+sen)
#         dp[i].add(sen+"+2")
#     for sen in dp[i-3]:
#         dp[i].add("3+"+sen)
#         dp[i].add(sen+"+3")
# for _ in range(n):
#    x = int(sys.stdin.readline())
#    print(len(dp[x]))

# 단순 DP 문제로 풀기

import sys
MAX = 10
n = int(sys.stdin.readline())
dp = [0 for _ in range(MAX+1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,MAX+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(n):
    print(dp[int(sys.stdin.readline())])