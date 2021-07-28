'''
4
bcdef
abcdefg
bcde
bcdef
------
3
2 1 1
'''

n = int(input())
l = {}
for i in range(n):
    k= input()
    if k in l:
        l[k]+=1 # 2. bcdef가 딕셔너리 안에 있으므로 2로 만들기
    else:
        l[k] = 1    # 1. bcdef가 없었으므로 1로 만들기
print(len(l))
for i in l:
    print(l[i], end=" ")    # 2 1 1
