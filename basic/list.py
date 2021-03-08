
"""리스트는 값들의 모음이다.
기본적으로 검색, 생성, 삭제, 수정이 가능하다.
"""

a = []
b = [1,2,3]
c = ["life", "is", "too", "short"]
d = [1, 2, ['life', 'is']]
tmp = d[-1][1]
print(tmp)


# a = [1, 2, 3]
# print(a[0] + a[2])
# print(a[-1])

"리스트 슬라이싱"
a = [1, 2, 3, 4, 5]
tmp = a[0:2]
print(tmp)

b = a[:2]
c = a[2:]
print(b)
print(c)

"리스트 연산하기"
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

"리스트 반복 (*)"
a = [1, 2, 3]
print(a * 3)

"리스트 길이"
print(len(a))

print(str(a[0]) +" good")

"리스트의 수정과 삭제"
a = [1, 2, 3]
a[2] = 4
print(a)
del a[1] # x번째 요소 삭제
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

"리스트 관련 함수"

"리스트 요소 추가(append)"
a = [1, 2, 3]
a.append(6)
print(a) # 1, 2, 3, 6

a.append([5, 6])
print(a) # [1, 2, 3, 6, [5, 6]]

a = [1, 4, 3, 2]
a.sort()
print(a) # 1, 2, 3, 4

a = ['a', 'c', 'b']
a.sort()
print(a) # a, b, c

"리스트 뒤집기(reverse)"
a = ['a', 'c', 'b']
a.reverse()
print(a) # b, c, a

"위치 반환(index)"
"갑이 존재하지 않으면 에러 발생 => ValueError"
a = [1, 2, 3]
print(a.index(2)) # 값 2의 인덱스 찾기 => 1
print(a.index(1)) # 값 1의 인덱스 찾기 => 0

"리스트에 요소 삽입(insert)"
a = [1, 2, 3]
a.insert(1, 10) # a[1] 위치에 10 삽입
print(a) # 1, 10, 2, 3

a = [1, 2, 3]
a.remove(2) # 값 2를 삭제
print(a) # 1, 3

a = [1, 2, 3, 3]
a.remove(3) # 값 3을 삭제. 처음 발견된 값을 삭제
print(a)

a = [1, 2, 3]
a.pop() # 맨 마지막 요소를 돌려주고 그 요소 삭제
print(a) # 1, 2
a.pop()
print(a) # 1

a = [1, 2, 3]
a.pop(2) # a[2] 요소를 돌려주고 그 요소는 삭제한다.
print(a) # 1, 2

"""리스트에 포함된 요소x의 개수 세기(count)"""
a = [1, 2, 3, 1]
tmp = a.count(1) # 1이라는 값의 개수 세기
print(tmp) # 2개

"""리스트 확장(extend)"""
""" 원래의 a 리스트에 추가할려는 리스트를 더한다. """
a = [1, 2, 3]
a.extend([4, 5])
print(a) # 1, 2, 3, 4, 5





