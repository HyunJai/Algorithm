# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
  2
  6
  4 3 2 1 3 4
  3
  1 3 2
'''
for t in range(int(input())):
    input()
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    left = lst[:min_list]
    right = lst[min_list+1:]
    if left == sorted(left, reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")
