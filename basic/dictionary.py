
"""
딕셔너리
Key를 통해 Value를 얻는다.
순차적으로 데이터를 검색하는 것이 아닌 해시값을 통해 해당 Value를 얻는다.
"""

"딕셔너리의 기본 형태"
# {key1 : Value1, key2 : Value2, key3 : value3}

dic = {'name' : 'pey',
       'phone' : '0119993323',
       'birth' : '1118'}
print(dic)

a = {1 : 'hi'}

a = {'a' : [1, 2, 3]}

"딕셔너리 쌍 추가, 삭제하기"
"딕셔너리 쌍 추가"
a = {1: 'a'}
a[2] = 'b'  # {2:'b'} 쌍 추가
print(a) # {1: 'a', 2: 'b'}

a['name'] = 'pey' # {'name' : 'pey'}
print(a) # {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = ["a", "b", "c", 3] # {3: [1,2,3]} 쌍 추가
print(a) #{1: 'a', 2: 'b', 'name': 'pey', 3: ['a', 'b', 'c', 3]}

"딕셔너리 요소 삭제하기"
del a[3] # 키 3에 해당하는 쌍을 삭제한다
# del a["key"] # 존재하지 않는 키를 삭제할 땐 에러 발생
# => KeyError: 'key'

"딕셔너리 사용하기"

"딕셔너리에서 Key를 사용해서 Value얻기"

grade = {'pey': 10, 'mike': 99}
print(grade['pey']) # 10
print(grade['mike']) # 99

a = {"good" : 100, "bad" : 0}
print(a["good"]) # 100
print(a["bad"]) # 0

a = {100 : "good" , 0 : "bad"}
print(a[100]) # "good"
print(a[0]) # "bad"

"딕셔너리 주의사항"
a = {1 : 'a', 1 : 'b'}  # 중복 키 값 넣기

print(a) # {1 : 'b'}  # {1 :'a'} 쌍이 무시된다

"key에 리스트는 사용할 수 없다. 리스트는 값이 변하기 때문에 키로 사용할 수 없다 "

# a = { [1,2] : 'hi'} # TypeError: unhashable type: 'list'
# a = { a : [1, 2]} # TypeError: unhashable type: 'dict'

"딕셔너리 관련 함수"

a = { 'name' : 'pey', 'phone': '0119993323', 'birth' : '1118' }
print(a.keys()) # dict_keys(['name', 'phone', 'birth']) 딕셔너리의 Key만을 모아서 객체를 돌려준다.

for k in a.keys():
    print(k)

"""
=> 출력
name
phone
birth
"""

"딕셔너리 객체를 리스트로 변환하기"
tmp = list(a.keys())
print(tmp) # ['name', 'phone', 'birth']

"Value 리스트 만들기(values)"

print(a.values()) # dict_values(['pey', '0119993323', '1118'])

"Key, Value 쌍 얻기(items)"

tmp = a.items()
print(tmp) # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
# Key와 Value의 쌍을 튜플로 묶은 값을 돌려준다.
tmp2 = list(tmp)
print(tmp2) # [('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')]
print(tmp2[0]) #  ('name', 'pey')
print(tmp2[1]) #  ('phone', '0119993323')

"Key:Value 쌍 모두 지우기(clear)"
a = { 'name' : 'pey', 'phone': '0119993323', 'birth' : '1118' }
a.clear() # 딕셔너리 안의 모든 요소를 삭제한다.
print(a) # {} 빈 딕셔너리

"Key로 Value 얻기(get)"
"get(x) x라는 Key에 대응되는 Value를 돌려준다."
a = { 'name' : 'pey', 'phone': '0119993323', 'birth' : '1118' }
print(a.get('name')) # pey
print(a.get('phone')) # 0119993323

# print(a['day']) # KeyError: 'day' 에러발생
print(a.get('day')) # 에러대신 None 반환. 존재하지 않는 키를 찾을때

"찾으려는 Key값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x, '디폴트 값') 사용 "
print(a.get('month', '10')) # 10 , 해당하는 month 키가 없어서 미리 설정해둔 10을 리턴한다.

"해당 Key가 딕셔너리 안에 있는지 조사하기(in)"
print('name' in a) # True
print('month' in a) # False

