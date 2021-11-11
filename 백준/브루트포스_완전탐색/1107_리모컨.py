import sys, itertools, bisect
MAX = 500000
goal = int(sys.stdin.readline())

n = int(sys.stdin.readline())

impossible_nums = list(map(int, sys.stdin.readline().split()))
list_nums = []
is_possible = [1 for i in range(MAX + 1)]


for i in range(1,6):
    nums = list(itertools.product(impossible_nums, repeat=i))
    for num in nums:
        temp_str = ""
        for s in num:
            temp_str += str(s)
        result = int(temp_str)
        if result <= MAX:
            is_possible[result] = 0

answer = goal - 100
# 확인해야하는것
# 1. 현재 채널에서 바로 갈 정도인가
if is_possible[goal]:
    answer = min(answer, len(goal))
# 2. 번호를 입력할 수 있는가
else:
    left = bisect.bisect_right(is_possible[:goal],1)
    right = goal + bisect.bisect_left(is_possible[goal+1:],1)
    print(f'left : {left}, right : {right}')
    #temp_num = min(left, right) + len(goal)
# 3. 
print(f'answer : {answer}')