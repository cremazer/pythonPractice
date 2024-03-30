# dictionary는 key와 value의 쌍으로 이루어진 자료형이다. (JSON과 비슷)
# dictionary는 {}로 묶어서 생성하며, key와 value는 ':'로 구분한다.
dic1 = {'name': 'Lucky', 'phone': '01012345678', 'birth': '0618'}
print(dic1)

# dictionary 요소 추가하기
dic1['address'] = 'Seoul'
print(dic1)

# dictionary 요소 삭제하기
del dic1['birth']
print(dic1)

# dictionary key를 사용하여 value 얻기
print(dic1['name'])
print(dic1['phone'])

# dictionary 주의 사항
# key는 고유한 값이므로 중복되는 key 값을 설정하면 하나를 제외한 나머지는 무시된다.
dic2 = {1: 'a', 1: 'b'}
print(dic2)  # {1: 'b'}

# dictionary 관련 함수
# keys() - key 리스트 만들기
dic3 = {'name': 'Lucky', 'phone': '01012345678', 'birth': '0618'}
print(dic3.keys())  # dict_keys(['name', 'phone', 'birth'])

# values() - value 리스트 만들기
print(dic3.values())  # dict_values(['Lucky', '01012345678', '0618'])

# items() - key, value 쌍 얻기
print(dic3.items())  # dict_items([('name', 'Lucky'), ('phone', '01012345678'), ('birth', '0618')])

# clear() - dictionary 요소 모두 지우기
dic3.clear()

# get() - key로 value 얻기
dic4 = {'name': 'Lucky', 'phone': '01012345678', 'birth': '0618'}
print(dic4.get('name'))  # Lucky
print(dic4.get('phone'))  # 01012345678
print(dic4.get('address'))  # None
# print(dic4['address'])  # KeyError: 'address'
