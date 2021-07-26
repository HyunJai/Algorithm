import sys
sys.stdin = open("AAA/input.txt", 'r')

n= int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 가장자리 만들어주는 방법
a.insert(0, [0]*n)
a.append([0]*n)

for x in a:
    x.insert(0, 0)
    x.append(0)
cnt=0

# 상,하,좌,우 탐색
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n+1):
    for j in range(1,n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

print(cnt)
