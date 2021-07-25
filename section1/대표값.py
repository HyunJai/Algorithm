N = 10
a = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]
min = 999999999
ave = round(sum(a)/N)

for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res=idx+1
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1
print(ave, res)

