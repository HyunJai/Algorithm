import sys
sys.stdin = open('HyunJae/CodeTest/input.txt','r')

n, m = map(int, input().split())
weight = list(map(int, input().split()))

cnt=0

weight.sort()
# 내가 푼 방식
for x in weight:
    x1 = max(weight)
    x2 = min(weight)
    if x1+x2>m:
        cnt+1
        weight.pop()
        weight.sort()
    elif x1+x2<=m:
        cnt+=1
print(cnt)

# 정보올림피아드 방식
while weight:
    if len(weight)==1:
        cnt+=1
        break
    if weight[0]+weight[-1]>m:
        weight.pop()
        cnt+=1
    else:
        weight.pop(0)
        weight.pop(-1)
        cnt+=1
