from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    pa, pb, pc = 0, 0, 0 # 각 배열의 커서
    na, nb  = len(a), len(b) # 각 배열의 원소수

    while pa < na and pb < nb: # pa와 pb를 비교하여 작은 값을 pc에 저장
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    while pa < na: # a에 남은 원소를 복사
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb: # b에 남은 원소를 복사
        c[pc] = b[pb]
        pb += 1
        pc += 1

if __name__ == '__main__':
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + len(b))
    print('정렬을 마친 두 배열의 병합 수행')

    merge_sorted_list(a, b, c) # 배열 a, b를 병합 -> c에 저장

    print('병합 완료')
    print(f'배열 a: {a}')
    print(f'배열 b: {b}')
    print(f'배열 c: {c}')
