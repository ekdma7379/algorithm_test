import sys, bisect

dp = []
n = int(sys.stdin.readline())

list_data = list(map(int, sys.stdin.readline().split()))
distinct_data = list(set(list_data)).sort()

for data in distinct_data:
    dp.append((bisect.bisect_left(data),bisect.bisect_right(data)))

for i in range(len(dp)):
    start = data[i][0]
    end = data[i][1]
    for j

