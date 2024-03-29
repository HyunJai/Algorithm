# 그리디 알고리즘은 보통 '정렬'

import sys
sys.stdin = open("AAA/input.txt", 'r')

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))
# meeting.sort() -> (1,2) (2,3), (3,4)...
meeting.sort(key=lambda x : (x[1], x[0]))
et=0
cnt=0
for s, e in meeting:
    if s>=et:
        et=e
        cnt+=1
print(cnt)
