

"함수"

"""
def 함수 이름(매개변수):
    수행할 문장1
    수행할 문장2
"""
def add(a, b): # 매개변수 a, b
    return a + b
# 함수의 이름은 add이고 입력으로 2개의 값을 받으며 결과값은 2개의 입력값을 더한 값이다.

a = 10
b = 20
tmp = add(a, b) # 인수
print(tmp)  # return 30

"매개변수와 인수"
"매개변수(parameter), 인수(arguments)"

"입력값이 없는 함수"
def say():
    return 'hello world'

tmp = say()
print(tmp) # hello world

"결괏값이 없는 함수"
def add(a, b):
    print("%d" % (a+b))

add(70, 80) # 150

# 결괏값은 오직 return 명령어로 돌려받는다.
# None은 거짓을 나타내는 자료형이다.

"입력값도 결괏값도 없는 함수"
def say():
    print('HI')

say() # HI

"매개변수 지정하여 호출하기"
def add(a, b):
    return a + b

result = add(a= 3, b = 7) # 순서 상관없이 지정하여 인자를 넘긴다.
print(result) # 10

result = add(b= 3, a = 7) # ""
print(result) # 10


"여러 개의 입력값을 받는 함수 만들기"

def add_many(*args): # *(임의로 정한 매개변수 이름)
    result = 0
    for i in args:
        result += i # args에 입력받은 모든 값을 더한다.
    return result

tmp = add_many(1,2)
print(tmp) # 3
tmp = add_many(1,2,3,4,5,6,7,8,9,10)
print(tmp) # 55


"example"

def add_mul(menu, *args):
    if menu == 'add':
        result = 0
        for i in args:
            result += i
    elif menu == 'mul':
        result = 1
        for i in args:
            result *= i
    return result

tmp = add_mul('add', 1,2,3,4,5)
print(tmp) # 15

tmp = add_mul('mul', 1,2,3,4,5)
print(tmp) # 120

"키워드 파라미터"
def print_keyword_args(**kwargs):
    print(kwargs)

print_keyword_args(a = 1) # {'a': 1}
print_keyword_args(name = 'dev', age = 13) # {'name': 'dev', 'age': 13}

"함수의 결괏값은 언제나 하나이다"

def add_and_mul(a, b):
    return a+b, a*b # 2개의 매개변수를 받아 더한 값과 곱한 값을 돌려준다

result = add_and_mul(3, 4)
print(result) # (7, 12), 튜플

"함수는 하나지만 2개의 결괏값처럼 받고 싶을때"
result1, result2 = add_and_mul(3, 4)
print(result1) # 7
print(result2) # 12

"매개변수에 초깃값 미리 설정하기"

def say_myself(name, old, man=True):
    print("my name is %s." % name )
    print("my old is %s." % old)
    if man:
        print('man')
    else:
        print('women')

say_myself('mike', '13')
# my name is mike.
# my old is 13.
# man

say_myself('kim', '20', False)
# my name is kim.
# my old is 20.
# women

"초기화시키고 싶은 매개변수는 항상 뒤쪽에 놓는다."
# def say_myself(name, man=True, old):
#     print("my name is %s." % name )
#     print("my old is %s." % old)
#     if man:
#         print('man')
#     else:
#         print('women')
#
# # SyntaxError: non-default argument follows default argument

# say_myself('user1', '20', False)

# "함수 지역변수"
# def vartest(a):
#     a = a + 1
#
# vartest(3)
# # print(a) # NameError: name 'a' is not defined

"lambda"
# lambda 매개변수1, 매개변수2, ... 매개변수를 사용한 표현식

add = lambda a, b: a+b
result = add(3, 4)
print(result) # 7

"lambda 표현식과 동일한 로직."
def add(a,b):
    return a+b
result = add(3,4)
print(result) # 7



