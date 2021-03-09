
"bool 자료형"
a = True
b = False

print(type(a)) # <class 'bool'>
print(type(b)) # <class 'bool'>

print(2 > 1) # True
print(2 < 1) # False

"""
값이 존재하면 참 
존재하지 않으면 거짓
"""

""" 예시 """
a = [1, 2, 3, 4]
while a:
    print(a.pop())
"""
4
3
2
1
"""

if []:
    print("참")
else:
    print("거짓")

# 거짓 출력한다.

"""
불 연산 자료형의 참과 거짓을 식별한다.
"""
print(bool('python')) # True
print(bool('')) # False







