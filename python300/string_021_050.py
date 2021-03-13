
"""
024 문자열 슬라이싱
문자열 거꾸로 출력하기
"""

string = "python"
print(string[::-1]) # nohtyp

"""
025 문자열 치환
하이푼을 재거하고 출력하기
"""

phone_number = "010-1234-5678"
print(phone_number.replace("-", "")) #01012345678

"""
027 문자열 다루기
url에 저장된 웹 페이지 주소에서 도메인을 출력하기
"""
url = "http://helloworld.kr"
url_split = url.split('.')
print(url_split[-1]) # kr
print(url_split[1])  # kr

"""
028 문자열은 immutable(수정할 수 없는)
문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있다.
"""

lang = 'python'
# lang[0] = 'P' # TypeError: 'str' object does not support item assignment

"""
030 replace 메서드
파이썬에서 문자열은 변결할 수 없는 자료형이다. 그래서 아래와 같은 경우 원본은 그대로 두고 새로운 문자열 객체를 리턴해준다.
"""

string = 'abcd'
string.replace('b', 'B')
print(string) # abcd

"""
040 strip 메서드
원본 문자열은 그대로 유지되고 공백이 제거된 새로운 문자열이 반환된다.
"""

data = ' kakao  '
data1 = data.strip()
print(data1) # kakao

"""
044 endswith 메서드
파일 이름이 문자열로 저장되어 있을 때 파일 이름이 'xlsx'로 끝나는지 확인하기.
"""

file_name = "report.xlsx"
print(file_name.endswith("xlsx")) # True
print(file_name.endswith("pdf")) # False

"""
046 startswith 메서드
startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인하기.
"""
file_name = "2020_report.xlsx"
print(file_name.startswith("2020")) # True
print(file_name.startswith("2100")) # False

"""
048 split 메서드
다음과 같이 문자열이 있을 때 btc와 krw로 나누기.
"""
ticker = "btc_krw"
lst = ticker.split("_")
print(lst) # ['btc', 'krw']

"""
049 split 메서드
다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
"""

date = "2020-10-20"
lst = date.split("-")
print(lst) # ['2020', '10', '20']