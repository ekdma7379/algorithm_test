import sys

MAX = 1000000

target = int(sys.stdin.readline())
answer = abs(100 - target)
M = int(sys.stdin.readline())

if M:
    Numbers = list(sys.stdin.readline().split())
else:
    Numbers = []

for num in range(MAX + 1):
    for N in str(num):
        if N in Numbers:
            break
    else:
        answer = min(answer, len(str(num)) +abs(num - target))
        #print(f'num : {num}, answer : {answer}')

print(answer)