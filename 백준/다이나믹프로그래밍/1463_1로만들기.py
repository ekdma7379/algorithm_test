import sys

n = int(sys.stdin.readline())

result_list = [n for i in range(n+1)]

result_list[n] = 0

for i in range(n,1,-1):
    if i % 3 == 0:
        share = i//3
        result_list[share] = min(result_list[share], result_list[i]+1)
    if i % 2 == 0:
        share = i//2
        result_list[share] = min(result_list[share], result_list[i]+1)
    result_list[i-1] = min(result_list[i-1], result_list[i]+1)

print(result_list[1])
