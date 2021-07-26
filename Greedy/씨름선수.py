# 그리디 알고리즘은 보통 '정렬'

import sys
sys.stdin = open("AAA/input.txt", 'r')

n = int(input())
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a,b))
# meeting.sort() -> (1,2) (2,3), (3,4)...
body.sort(reverse=True)    # 내림 차순으로 정렬하여 키를 비교
largest = 0
cnt = 0
for x, y in body:
    if y > largest:
        largest=y
        cnt+=1
print(cnt)