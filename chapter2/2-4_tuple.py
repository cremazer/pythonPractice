# 튜플은 리스트와 달리 요소를 변경할 수 없다.
# Mutable(가변) - 리스트, 딕셔너리, 집합
# Immutable(불변) - 정수, 실수, 문자열, 튜플

# 튜플은 소괄호()를 사용하여 만들 수 있다.
t1 = ()
# 튜플에서 요소가 하나인 경우에는 반드시 콤마(,)를 붙여야 한다.
t2 = (1,)
# 튜플은 괄호를 표현하는 것이 일반적이다.
t3 = (1, 2, 3)
# 괄호를 생략해도 튜플로 인식한다.
t4 = 1, 2, 3

# 튜플의 요소를 삭제하기
t5 = (1, 2, 'a', 'b')
# del 함수를 사용하여 튜플의 요소를 삭제할 수 없다.
# del t5[0]  # TypeError: 'tuple' object doesn't support item deletion

# 튜플 인덱싱
t6 = (1, 2, 'a', 'b')
print(t6[0])  # 1

# 튜플 슬라이싱
t7 = (1, 2, 'a', 'b')
print(t7[1:])  # 1번 인덱스 이상 출력 -> (2, 'a', 'b')

# 튜플 더하기
t8 = (1, 2, 'a', 'b')
t9 = (3, 4)
print(t8 + t9)  # (1, 2, 'a', 'b', 3, 4)
# 새로운 튜플로 출력할 수 있다.
t10 = t8 + t9
print(t10)  # (1, 2, 'a', 'b', 3, 4)

# 튜플 곱하기
t11 = (1, 2, 'a', 'b')
print(t11 * 3)  # (1, 2, 'a', 'b', 1, 2, 'a', 'b', 1, 2, 'a', 'b')

# 튜플 길이 구하기
t12 = (1, 2, 'a', 'b')
print(len(t12))  # 4
