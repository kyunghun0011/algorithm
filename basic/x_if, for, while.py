
"""
조건
"""

"""
x in 리스트
x in 튜플
x in 문자열

x not in 리스트
x not in 튜플
x not in 문자열
"""

tmp = 1 in [1, 2, 3]
tmp2 = 5 in [1, 2, 3]
print(tmp) # True
print(tmp2) # False

tmp = 'a' in ('a', 'b', 'c')
tmp2 = 'j' not in ('python')
print(tmp) # True
print(tmp2) # True

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시")
else:
    print("도보")
# => 택시

"조건문에서 아무런 일도 하지 않도록 하고 싶을때 PASS"

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print('걸어서 가기')
# =>

pocket = ['paper', 'cellphone', 'money']
drink = True
if 'snack' in pocket:
    print("과자")
elif drink:
    print('음료수 마시기')
else:
    print("도보")
# => 음료수 마시기

"조건부 표현식"
"조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우"

score = 100
message = "success" if score >= 60 else "failure"
print(message) # success

score = 40
message = "success" if score >= 60 else "failure"
print(message) # failure


"""
while

while 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
"""

treeHit = 0
while treeHit < 10:
    treeHit += 1
    print(treeHit)
    if treeHit == 10:
        print("클리어")

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 클리어


coffee = 10
money = 300
while money:
    print('커피?')
    coffee -= 1
    print(coffee)
    if coffee == 0:
        print("empty!")
        break
# 커피?
# 9
# 커피?
# 8
# 커피?
# 7
# 커피?
# 6
# 커피?
# 5
# 커피?
# 4
# 커피?
# 3
# 커피?
# 2
# 커피?
# 1
# 커피?
# 0
# empty!

"while문의 맨 처음으로 돌아가기"
a = 0
while a < 10:
    a = a +1 # a += 1
    if a % 2 == 0: continue  #  짝수일때 맨 처음 문으로 돌아간다. 아래는 실행하지 않는다.
    print(a)

# 1
# 3
# 5
# 7
# 9

print("*" * 50)
"""
for문

for 변수 in 리스트(또는 튜플, 문자열)
    수행할 문장1
    수행할 문장2
    ....
"""

"for문의 기본 구조"

l1 = ['one', 'two', 'three']
for number in l1:
    print(number)
# one
# two
# three

a = [(1,2), (3,4), (5, 6)]
for (first, last) in a:
    print(first + last)
# 3
# 7
# 11

"for문 예시"
score_list = [90, 25, 67, 45, 80]
number = 0
for score in score_list:
    number += 1
    if score >= 60:
        print("%d번 학생은 합격." % number)
    else:
        print("%d번 학생은 불합격." % number)
# 1번 학생은 합격.
# 2번 학생은 불합격.
# 3번 학생은 합격.
# 4번 학생은 불합격.
# 5번 학생은 합격.

"for문과 continue"
score_list = [90, 25, 67, 45, 80]
number = 0
for score in score_list:
    number += 1
    if score < 60: continue # 60점 미만 제외
    print("%d번 학생 합격." % number )
# 1번 학생 합격.
# 3번 학생 합격.
# 5번 학생 합격.

"for문과 range함수"
"range(시작 숫자, 끝 숫자)  끝숫자가 10이라고 한다면 9까지 포함된다."

a = range(10)
print(a) # range(0, 10)
print(list(a)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = range(11)
print(b) # range(0, 11)
print(list(b)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"range 함수의 예시 살펴보기"
add = 0
for i in range(1, 11): # 1부터 10까지 숫자를 데이터로 갖는 객체이다.
    add += i
    print(add)
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# 55

print('*' * 50)
socre_list = [90, 25, 46, 75, 84]
# print(len(score_list)) # 5

for score in range(len(socre_list)):
    # print(socre_list[score])
    if score_list[score] < 60: continue
    print("%d번 학생 합격." % (score + 1) )

# 1번 학생 합격.
# 3번 학생 합격.
# 5번 학생 합격.


"리스트 내포 사용하기(list comprehension)"
"[표현식 for 항목 in 반복 가능 객체 if 조건]"
"""
[표현식 for 항목 in 반복 가능 객체 if 조건1"
       for 항목 in 반복 가능 객체 if 조건2
       for 항목 in 반복 가능 객체 if 조건3]
"""


a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)

print(result) # [3, 6, 9, 12]
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)
Even = [num * 10 for num in a if num % 2 == 0]
odd  = [num * 10 for num in a if num % 2 != 0]
print(Even) # [20, 40]
print(odd) # [10, 30]

"구구단 예제"

result = [x * y for x in range(2, 10)
                for y in range(1, 10)
          ]
print(result)
# [2, 4, 6, 8, 10, 12, 14, 16, 18,
# 3, 6, 9, 12, 15, 18, 21, 24, 27,
# 4, 8, 12, 16, 20, 24, 28, 32, 36,
# 5, 10, 15, 20, 25, 30, 35, 40, 45,
# 6, 12, 18, 24, 30, 36, 42, 48, 54,
# 7, 14, 21, 28, 35, 42, 49, 56, 63,
# 8, 16, 24, 32, 40, 48, 56, 64, 72,
# 9, 18, 27, 36, 45, 54, 63, 72, 81]