from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬"""
    ccnt = 0 # 비교 횟수
    scnt = 0 # 교환 횟수
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            ccnt += 1
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                scnt += 1
                last = j # 마지막 정렬한 인덱스 저장
        k = last # 정렬이 끝난 부분은 생략하고 탐색

    print(f'ccnt = {ccnt}')
    print(f'scnt = {scnt}')

if __name__ == '__main__':
    print('버블 정렬')
    num = int(input('원소 수를 입력.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)

    print('정렬 후')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
