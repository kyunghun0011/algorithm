
print("sorted() 함수 사용하여 정렬")
num = int(input('원소 수 입력.: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

x = sorted(x)
print('오름차순 정렬')
print(x)

print('내림차순 정렬')
x = sorted(x, reverse = True)
print(x)
