# 유용하게 사용되는 함수
---
  
## 1. 문자열 관련 함수
- any() : 인자로 받은 반복가능한 자료형(iterable)중 단 하나라도 참(True)이 있으면 참(True)를 반환하는 함수
- str.isalnum() : a-z, A-Z, 0-9 포함하면 True
- str.isalpha() : a-z, A-z 포함하면 True
- str.isdigit() : 0-9 포함하면 True
- str.islower() : 소문자 포함하면 True
- str.isupper() : 대문자 포함하면 True
- str.ljust() : Bae---------- 
- str.center() : -----Bae-----
- str.rjust() : ----------Bae
  
## 2. 시간 관련 함수
- datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z') : Sun 10 May 2015 13:54:36 -0700
- timedelta.total_seconds() : 기간에 포함된 총 시간을 초(seconds)로 반환
  
## 3. 그룹 관련 함수
- itertools.groupby() : 함수를 사용하면 혈액형별로 묶어 데이터를 분류함

## 4. 개수 관련 함수

- collections.OrderedDict() : 입력된 아이템들(items)의 순서를 기억하는 Dictionary 클래스
- collections.Counter() : 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용되는 객체로 딕셔너리를 리턴함
- collections.Counter().most_common(3) : 동일한 값의 자료가 몇개인지 3개까지만 파악하는데 사용되는 객체

## 5. 정규식 관련 함수
- [a-zA-Z] : 알파벳 모두
- [0-9] : 숫자 모두
- re.match() : 문자열의 처음부터 정규식과 매치되는지 조사
- re.search() : 문자열의 전체를 검색하여 정규식과 매치되는지 조사
- re.findall() : 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려줌
- re.finditer() : 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려줌
```
  import re
  re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
  
  {1,3} : extension의 최대 길이가 3
```


# 🍯'팁'
- 정답제출시 *를 붙여주면 리스트가 풀림
```
  예시 1
  
  a = [1, 2, 3, 4, 5]
  print(a)
  >> [1, 2, 3, 4, 5]
  print(*a)
  >> 1 2 3 4 5
```
```
  예시 2
  
  from itertools import groupby
  
  print(*[(len(list(c)), int(k)) for k, c in groupby(input())]) 
                    
```
```
  예시 3
  
  [print(letter) for letter in letters]
  >>>('b', 3)
     ('a', 2)
     ('c', 2)
     
  [print(*letter) for letter in letters]
  >>>b 3
     a 2
     c 2 
```
- 그리디 문제 = sort()로 대부분
- 고난이도 수학 문제 = Scale, Rotation, 좌표 이동 문
