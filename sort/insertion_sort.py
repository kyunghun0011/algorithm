from typing import MutableSequence

"""
아직 정렬되지 않은 부분의 맨 앞 원소를 정렬된 부분의 알맞은 위치에 삽입합니다.
"""
def insertion_sort(a: MutableSequence) -> None:
    """단순 삽입 정렬(shuttle sort)"""
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

if __name__ == '__main__':
    print('단순 삽입 정렬')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    insertion_sort(x)

    for i in range(num):
        print(f'x[{i}] = {x[i]}')
