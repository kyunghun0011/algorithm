
"""
집합 자료형
"집합 자료형의 특징"
"중복을 허용하지 않는다."
"순서가 없다(Unordered)"
중복을 허용하지 않는 특징을 이용하여 자료형의 중복을 제거하기 위한
필터 역할로 종종 사용한다.
"""

"set 기본 형태"
s0 = set()
s1 = set([1, 2, 3])
s2 = set("hello")
print(s2) # {'o', 'l', 'h', 'e'} , {'e', 'o', 'l', 'h'} 매번 출력결과가 달라진다.

s1 = set([1,2,3])
l1 = list(s1)
print(l1) # [1, 2, 3]
print(l1[0]) # 1

t1 = tuple(s1) # 튜플로 변환
print(t1) # (1, 2, 3)
print(t1[0]) # 1

"교집합, 합집합, 차집합 구하기"
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

"교집합"
print(s1 & s2)

print(s1.intersection(s2))

"합집합"
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

"차집합"
print(s1 - s2) # {1, 2, 3}

print(s2 - s1) # {8, 9, 7}

print(s1.difference(s2)) # {1, 2, 3}

print(s2.difference(s1)) # {8, 9, 7}

"집합 자료형 관련 함수"

"값 1개 추가하기(add)"
s1 = set([1, 2, 3])
s1.add(4)
print(s1) # {1, 2, 3, 4}

"값 여러 개 추가하기(update)"
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1) # {1, 2, 3, 4, 5, 6}

"특정 값 제거하기(remove)"
s1 = set([1, 2, 3])
s1.remove(2)
print(s1) # {1, 3}
