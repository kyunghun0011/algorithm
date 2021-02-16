from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬"""
    ccnt = 0 # 비교 횟수
    scnt = 0 # 교환 횟수
    n = len(a)
    for i in range(n - 1):
        exchange = 0 # 패스 교환 횟수
        for j in range(n - 1, i, -1):
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                exchange += 1
        if exchange == 0: # 더 이상 자리 바꿀 원소가 없을때 break
            break

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
