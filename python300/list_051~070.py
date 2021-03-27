
"""
051 리스트생성
"""
movie_rank = ['닥터스트레인지', '스플릿', '럭키']

"""
052 리스트에 원소 추가
"""
movie_rank = ['닥터스트레인지', '스플릿', '럭키']
movie_rank.append("배트맨")
print(movie_rank)

"""
053 슈퍼맨을 닥터 스트레인지와 스플릿 사이에 추가하라.
사용할 함수 : insert(인덱스, 원소)
"""
movie_rank = ['닥터스트레인지', '스플릿', '럭키']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

"""
054 '럭키'를 삭제하라
"""
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove('슈퍼맨')
del movie_rank[2]
print(movie_rank)

"""
055 '스플릿'과 '배트맨'을 삭제하라
"""
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[2]  # !삭제 후 리스트는 새로 인덱싱된다.
print(movie_rank) # '닥터 스트레인지', '슈퍼맨',  '럭키', '배트맨'
del movie_rank[2]  # 새로운 인덱스 고려하여 삭제한다.
print(movie_rank) # '닥터 스트레인지', '슈퍼맨',   '배트맨'

"""
056 lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
"""
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

lang3 = lang1 + lang2
print(lang3)

"""
057 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
"""
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums)) # 7
print(min(nums)) # 1

"""
058 다음 리스트의 합을 출력하라
"""
nums = [1, 2, 3, 4, 5]
print(sum(nums)) # 15

"""
059 다음 리스트에 저장된 데이터의 개수를 화면에 구하라.
"""
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook)) # 12

"""
060 다음 리스트의 평균을 출력하라.
"""
nums = [1, 2, 3, 4, 5]
print(sum(nums) / len(nums)) # 3.0

"""
061 price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
"""
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 출력 예시:
# [100, 130, 140, 150, 160, 170]

"""
062 슬라이싱을 사용해서 홀수만 출력하라.
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2]) # 1, 3, 5, 7, 9

# 실행 예:
# [1, 3, 5, 7, 9]

"""
063
슬라이싱을 사용해서 짝수만 출력하라.
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2]) # 2, 4, 6, 8, 10

# 실행 예:
# [2, 4, 6, 8, 10]

"""
064
슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
"""

nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 실행 예:
# [5, 4, 3, 2, 1]

"""
065
interest 리스트에는 아래의 데이터가 바인딩되어 있다.
"""
interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
print(interest[0], interest[2])

# 출력 예시:
# 삼성전자 Naver

"""
066 join 메서드
interest 리스트에는 아래의 데이터가 바인딩되어 있다.
"""
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
print(" ".join(interest))

# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우

"""
067 join 메서드
interest 리스트에는 아래의 데이터가 바인딩되어 있다.
"""
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우

"""
068 join 메서드
interest 리스트에는 아래의 데이터가 바인딩되어 있다.
"""

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
print("\n".join(interest))

# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우

"""
069 문자열 split 메서드
회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
"""
string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.
interest = string.split("/")
print(interest)

# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']

"""
070 리스트에 있는 값을 오름차순으로 정렬하세요.
"""
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data) # [1, 2, 3, 4, 5, 9, 10]

tmp = sorted(data)
print(tmp) # [1, 2, 3, 4, 5, 9, 10]