
# 수식적으로 아이디어가 아닌 원초적으로 푼 방법
# import sys, math

# goal = int(sys.stdin.readline())

# cnt = 0
# for i in range(goal//2+1):
#     n = goal-i
#     r = i
#     total = math.factorial(n)//(math.factorial(n-r)*math.factorial(r))
#     cnt += total

# print(cnt % 10007)

# 아이디어 
# 1. 공간이 2x(n-1) -> 2xn 크기로 증가할 때 2x1 크기만큼만 증가하는 경우

# 이 경우는 2x1 크기의 타일이 한 개 들어가는 경우밖에 없기 때문에 2x(n-1) 크기의 직사각형에 타일을 배치하는 방법의 수만큼만 더해주면 된다.

# 2. 공간이 2x(n-2) -> 2xn 크기로 증가할 때 2x2 크기만큼만 증가하는 경우

# 이 경우는 2x1 크기의 타일이 두 개가 들어갈 수 있다. 하지만 타일은 세워서 배치하는 경우 1번과 겹치는 경우이기 때문에 계산하지 않는다. 따라서 2x1 타일이 가로로 두 개 배치되는 경우만 고려하면 된다.

# 3. 공간이 2x(n-3) -> 2xn 크기로 증가할 때 2x3 크기만큼만 증가하는 경우

# 1, 2번의 경우와 중복되기 때문에 고려하지 않는다.

import sys
n = int(sys.stdin.readline())

dp = [0 for i in range(n+1)]

dp[1] = 1

dp[2] = 2

for i in range(3,n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n]%10007)