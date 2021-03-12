"파이썬 내장 모듈"

"all"
"""
반복 가능한 자료형 x를 입력 인수로 받으며 x가 참이면 True 것짓이 하나라도 있으면 False 반환
반복 가능한 자료형 ( 리스트, 튜플,문자열,딕셔너리 ) for문으로 출력가능
"""
tmp = all([1, 2, 3])
print(tmp) # True

tmp = all([1, 2, 3, 0])
print(tmp) # False


"any"
"""
any(x) x 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대
"""

tmp = any([1,2,3,0])
print(tmp) # True

tmp = any([0, False, ""])
print(tmp) # False


"chr"
"""
아스키 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이디.
"""
print(chr(97)) # 'a'
print(chr(48)) # 0

"dir"
"""
객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
"""
print( dir([1,2,3]))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
# '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
# '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
# '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
# 'pop', 'remove', 'reverse', 'sort']

print( dir({'name':'good'}))
#['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
# '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

"divmod"
"""
divmod(a,b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
"""
print(divmod(7, 3)) # (2, 1)


"enumerate"
"""
'열거하다'라는 뜻을 가진 이 함수는 순서가 있는 자료형 (리스트, 튜플, 문자열)을 입력으로 받아
인덱스 값을 포함하는 enumerate 객체를 돌려준다.
"""

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# 0 body
# 1 foo
# 2 bar

"eval"
"""
eval(expression)은 실행 가능한 문자열(1+2, 'hi' + 'a')을 입력으로 받아 
문자열을 실행한 결괏값을 돌려주는 함수이다.
예로 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다.
"""
print(eval('1+2')) # 3
print(eval("'hi' + 'a'")) # hia
print(eval('divmod(4, 3)')) # (1, 1)


"filter"
"""
무엇을 걸러낼 때 사용하는 함수이다. 첫 번째 인수로 함수 이름, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서 돌려준다.
"""

# example
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 4, 0, -2, 9])) # [1, 4, 9]

# example using by filter
def positive2(x):
    return x > 0

print(list(filter(positive2, [1, -3, 4, 0 , 7, -6]))) # [1, 4, 7]

tmp = list(filter(lambda x: x > 0, [1, -3, 2, 0, -6, 8]))
print(tmp) # [1, 2, 8]

"isinstance"
"""
isinstance(object, class)는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
"""

class NotPerson: pass
class Person: pass

a = Person()
print(isinstance(a, Person)) # True
print(isinstance(a, NotPerson)) # False

"len"
"""
len(s) 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.
"""
print(len("python")) # 6
print(len([1,2,3,4])) # 4

"list"
"""
list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
"""
lst = "python"
print(type(lst)) #<class 'str'>

lst = list("python") # s를 입력받아 리스트로 돌려주는 함수
print(lst)
print(type(lst)) #<class 'list'>

"리스트를 입력으로 줬을 때 복사하여 돌려준다."
a = [1, 2, 3]
b = list(a)
print(b) # [1, 2, 3]
print(id(a)) # 139877708250320
print(id(b)) # 139877683891568

"map"
"""
map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
"""

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result) # [2, 4, 6, 8]

def two_times2(x): return x * 2

tmp = list(map(two_times2, [1, 2, 3, 4]))
print(tmp) # [2, 4, 6, 8]

"lambda"
tmp = list(map(lambda a: a*2, [1, 2, 3, 4]))
print(tmp) # [2, 4, 6, 8]

"max"
print( max([1, 2, 3])) # 3

"min"
print( min([1, 2, 3])) # 1


"open"
"""
open(filename, [mode]) '파일 이름'과 '읽기 방법'을 입력받아 파일 객체를 돌려주는 함수이다.
읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.
"""
"""
w : 쓰기 모드
r : 읽기 모드
a : 추가 모드
b : 바이너리 모드
"""

"파일 생성"
# f = open("새파일.txt", 'r')
# f = open("새파일.txt", 'w')
# f = open("binary_file", 'rb')
# f.close()
#
# fappend = open("append_mode.txt", 'a')
# fappend.close()

"tuple"
"""
tuple(iterable) 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다.
"""

tmp = tuple("abc")
print(tmp) # ('a', 'b', 'c')

tmp = tuple([1, 2, 3])
print(tmp) #(1, 2, 3)

"zip"
"""
zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
*iterable : 반복 가능한 자료형(iterable) 여러 개를 입력할 수 있다는 의미이다.
"""

print(list(zip([1,2,3], [4,5,6])))  # [(1, 4), (2, 5), (3, 6)]



