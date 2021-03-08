
"""튜플은 상수라고 생각하면 편하다.
그 이유는 값을 변경할 수 없다.
"""
"튜플의 간단한 예제"
t1 = ()
t2 = (1, )
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
# t3[2] = 2 #TypeError: 'tuple' object does not support item assignment

"튜플 요솟값을 삭제하려 할 때 에러 발생"
t1 = (1, 2, 'a', 'b')
# del t1[0] # TypeError: 'tuple' object doesn't support item deletion

"튜플 요솟값을 변경하려 할 때 에러 발생"
# t1[1] = 'c' # TypeError: 'tuple' object does not support item assignment

"튜플 다루기"

"인덱싱"
t1 = (1, 2, 'a', 'b')
tmp = t1[0]
print(tmp)
tmp = t1[2]
print(tmp)

"슬라이싱"
tmp = t1[2:]
print(tmp) # ('a', 'b')

"튜플 더하기"
t2 = (3, 4)
tmp = t1 + t2
print(tmp) # (1, 2, 'a', 'b', 3, 4)

"튜플 곱하기"
tmp = t2 * 4
print(tmp) # (3, 4, 3, 4, 3, 4, 3, 4)

"튜플 길이 구하기"
print(len(tmp)) # 8

"튜플에 값을 추가할 순 없지만 새로운 튜플만들어서 더할 수 있다."
t3 = (1, 2, 3)
tmp = (4, )
print(t3 + tmp) # 1, 2, 3 4



