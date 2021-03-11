
"클래스(Class)"
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def status(self):
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

print(cal1.status())

print('*' * 50)


"클래스 구조"
class FourCal:
    pass

a = FourCal()
print(type(a)) # <class '__main__.FourCal'>

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4, 2) # 객체 a가 자동으로 전달된다 => self
print(a.first) # 4
print(a.second) # 2

# a -> self
# 4 -> first
# 2 -> second

a = FourCal()
b = FourCal()
a.setdata(4, 2)
print(a.first) # 4
b.setdata(3, 7)
print(b.first) # 3

print(id(a)) # 139809146090128
print(id(b)) # 140637784924816

print(id(a.first)) # 11167744
print(id(b.first)) # 11167712

# => 서로 다른 객체이므로 각가 객체에 값을 대입해도 영향이 가지 않는다.
# 객체 주소 값이 서로 다르므로 각각 다른 곳에 그 값이 저장된다.

"add, mul, sub, div class"

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

"객체 생성시 생성자를 통해 멤버변수 초기화"

# a = FourCal() # TypeError: __init__() missing 2 required positional arguments: 'first' and 'second'
a = FourCal(4, 2) # 생성자를 활용한 멤버변수 초기화
b = FourCal(3, 8)

# 메서드를 활용한 초기화
# a.setdata(4, 2)
# b.setdata(3, 8)

print(a.add()) # 6
print(a.mul()) # 8
print(a.sub()) # 2
print(a.div()) # 2.0

print(b.add()) # 11
print(b.mul()) # 24
print(b.sub()) # -5
print(b.div()) # 0.375

"클래스 상속"
"class 클래스이름(상속할 클래스 이름)"

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

inherited_obj = MoreFourCal(4, 2)
print(inherited_obj.add()) # 6
print(inherited_obj.mul()) # 8
print(inherited_obj.sub()) # 2
print(inherited_obj.div()) # 2.0

print(inherited_obj.pow()) # 16

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0: # 0으로 나누려고 할때 예외 처리 (ZeroDivisionError 발생하지 않도록 처리)
            return 0
        else:
            return self.first / self.second

inherited_obj = SafeFourCal(4, 0)
print(inherited_obj.div()) # 0


"클래스 변수"
"객체 변수와는 다른 클래스 변수를 값을 변경하려고 할때" \
"클래스 변수는 굥유된다."
class Family:
    lastname = "김"

print(Family.lastname) # 김

a = Family()
b = Family()
print(a.lastname) # 김
print(b.lastname) # 김

Family.lastname = "박" # 클래스 변수 수정

print(a.lastname) # 박
print(b.lastname) # 박

"id함수를 통해 클래스 변수가 공유된다는 사실을 증명"
print(id(Family.lastname)) # 139726601609088
print(id(a.lastname)) # 139726601609088
print(id(b.lastname)) # 139726601609088
