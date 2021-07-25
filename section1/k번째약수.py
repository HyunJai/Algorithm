cnt=0

n = 6
k = 3

for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break

else:
    print(-1)
