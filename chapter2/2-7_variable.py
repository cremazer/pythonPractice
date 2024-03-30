a = [1, 2, 3]
b = a
a[1] = 4
print(a)  # [1, 4, 3]
print(b)  # [1, 4, 3]

# a와 b는 동일한 리스트 객체를 가리키고 있기 때문에 a의 요소를 변경하면 b도 변경된다.
# a와 b는 동알한 id를 가지고 있다.
print(id(a))
print(id(b))

# copy() 함수를 사용하여 복사하면 다른 id를 가지게 된다.
c = a.copy()
a[2] = 5
print(a)  # [1, 4, 5]
print(c)  # [1, 4, 3]
# a와 c는 다른 리스트 객체를 가리키고 있기 때문에 a의 요소를 변경해도 c는 변경되지 않는다.
# a와 c는 다른 id를 가지고 있다.
print(id(a))
print(id(c))

(a, b) = ('python', 'life')
print(a)  # python
print(b)  # life

a = b = 'python'
print(a)
print(b)

# 튜플을 사용하면 간단하게 값을 서로 바꿀 수 있다.
a, b = b, a

# 어떤 프로그래밍 언어든 그 언어의 자료형을 알고 이해할 수 있다면, 그 언어의 기본을 이해한 것이다.