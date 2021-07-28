# 유용하게 사용되는 함수
---
  
## 1. 문자열 관련 문제
- any() : 인자로 받은 반복가능한 자료형(iterable)중 단 하나라도 참(True)이 있으면 참(True)를 반환하는 함수
- str.isalnum() : a-z, A-Z, 0-9 포함하면 True
- str.isalpha() : a-z, A-z 포함하면 True
- str.isdigit() : 0-9 포함하면 True
- str.lower() : 소문자 포함하면 True
- str.upper() : 대문자 포함하면 True
- str.ljust() : Bae---------- 
- str.center() : -----Bae-----
- str.rjust() : ----------Bae
  
## 2. 시간 관련 문제
- datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z') : Sun 10 May 2015 13:54:36 -0700
- timedelta.total_seconds() : 기간에 포함된 총 시간을 초(seconds)로 반환
  
## 3. 그룹 관련 문제
- itertools.groupby() : 함수를 사용하면 혈액형별로 묶어 데이터를 분류함

# 🍯'팁'
- 정답제출시 *를 붙여주면 리스트가 풀림
```
  a = [1, 2, 3, 4, 5]
  print(a)
  >> [1, 2, 3, 4, 5]
  print(*a)
  >> 1 2 3 4 5
```
```
  from itertools import groupby
  
  # 예시 1
  print(*[(len(list(c)), int(k)) for k, c in groupby(input())]) 
  
  # 예시 2
  for k,c in groupby(input()):
    print((len(list(c)), int(k)), end=' ')                      
```
- 그리디 문제 = sort()로 대부분 
