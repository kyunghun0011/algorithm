
print('hello world')

a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[4:])

array = [i  for i in range(20) if i % 2 == 1]
print(array)

############
n = 3
m = 4
array = [[0] * m for _ in range(n)] # N * M 크기의 2차원 리스트
print(array)
