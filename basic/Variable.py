
"""
변수 이름 = 변수에 저장할 값
"""

# 변수
"""
리스트 자료형(객채)이 자동으로 메모리에 생성되고 
변수 a는 [1, 2, 3] 리스트가 저장된 메모리의 주소를 가리키게 된다.
"""
a = [1, 2, 3]
b = a
print( id(a) ) # 140186676830848

"""
리스트 복사
"""
print( id(a) ) # 140186676830848 , 동일한 객체를 가리킨다.
print( id(b) ) # 140186676830848

a[1] = 4
print(b) # [1, 4, 3] , 값이 동일하게 변경된다.

" [:] 사용하여 값만 복사 "
a = [1, 2, 3]
b = a[:] # 리스트 a의 처음 요소부터 끝 요소까지 슬라이싱
a[1] = 4
print(a) # [1, 4, 3]
print(b) # [1, 2, 3]

"copy 모듈 사용"
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(a) # [1, 2, 3]
print(b) # [1, 2, 3]
print(id(a)) # 139942909954000
print(id(b)) # 139942935616640

tmp = a is b
print(tmp) # False

a = [4, 5, 6]
b = [4, 5, 6]
tmp = a is b
print(tmp) # False

"변수를 만드는 여러 가지 방법"
"튜플로 변수에 값을 대입"
a, b = ('python', 'Life')
(a, b) = 'python', 'Life'

print(a) # python
print(b) # Life

"리스트로 변수에 값 대입"
[c, d] = ['python', 'life']
print(c)
print(d)

"값 서로 swap 하기 "
a = 10
b = 20
a, b = b, a
print(a) # 20
print(b) # 10
