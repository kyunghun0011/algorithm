from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬"""
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0          # 검색 범위의 맨 앞 원소 인덱스
        pr = i - 1      # 검색 범위의 맨 끝 원소 인덱스

        while True:
            pc = (pl + pr) // 2 # 검색 범위의 가운데 원소 인덱스
            if a[pc] == key:    # 검색 성공
                break
            elif a[pc] < key:
                pl = pc + 1     # 검색 범위를 뒤쪽 절반으로 좁힘
            else :
                pr = pc - 1     # 검색 범위를 앞쪽 절반으로 좁힘
            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1     # 삽입해야 할 위치의 인덱스

        for j in range(i, pd, -1):
            a[j] =  a[j - 1]
        a[pd] = key

# def binary_insertion_sort2(a: MutableSequence) -> None:
#     """라이브러리 사용"""
#     for i in range(1, len(a)):
#         bisect.insort(a, a.pop(i), 0, i)

if __name__ == "__main__":
    print("이진 삽입 정렬 수행")

    num = int(input("원소 수 입력.: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    binary_insertion_sort(x)    # 배열 x를 이진 삽입 정렬

    print("오름차순으로 정렬.")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

"""
파이썬 표준 라이브러리 bisect 모듈 insort() 함수 모듈 사용가능.
"""
