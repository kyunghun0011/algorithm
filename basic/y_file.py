
"파일 입출력"


"readLine"
f = open("C:/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

while 1:
    data = input()
    if not data: break
    print(data)

f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

"파일 새로운 내용 추가하기"
f = open("C:/doit/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()