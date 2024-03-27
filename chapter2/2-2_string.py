# 문자열 타입 str
a = "Life is too short, You need Python"
b = "a"
c = "123"
print(a)
print(type(a))

d = "Hello, 'World!'"
print(d)

e = "Hello, \"World!\""
print(e)

# 줄바꿈
f = "Life is too short\n You need Python."
print(f)

g = '''Life is too short,
You need Python, too.
'''
print(g)

# 문자열 더하기
head = "Python"
tail = " is fun."
print(head + tail)

# 문자열 곱하기 = 문자열과 숫자를 곱할 수 있다.
print(head * 2)

# 문자열 길이 구하기 = len 함수
print(len(head))

# 문자열 인덱싱 = 문자열에서 특정 문자를 뽑아내는 것, 0부터 시작한다.
h = "Life is too short, You need Python"
print(h[3]) # e 출력

# 문자열 슬라이싱 = 문자열에서 단어를 뽑아내는 것, 0부터 시작한다.
print(h[0:4]) # Life 출력

# 문자열 간격
print(h[0:4:2]) # Lf 출력
print(h[::2]) # Lf stosot o edPto 출력

# 문자열 포매팅
count = 3
sentence = "I eat %d apples." % count
print(sentence)

count = 3
fruit = "apples"
sentence = "I eat %d %s." % (count, fruit)
print(sentence)

# 문자열 포매팅 - % 사용 (% 자체를 출력하려면 2개 입력한다)
percent = 80
sentence = "I got %d%% on the test." % percent
print(sentence)

# 문자열 포매팅 - 소수점 둘째자리까지 표현
percent = 80.123
sentence = "I got %.2f%% on the test." % percent
print(sentence)

# 문자열 포매팅 - format 함수 사용
name = "Lucky"
age = 43
sentence = "My name is {0} and I'm {1} years old.".format(name, age)
print(sentence)

# 문자열 포매팅 - format 함수 사용 (이름으로 넣기)
name = "Lucky"
age = 43
sentence = "My name is {name} and I'm {age} years old.".format(name=name, age=age)
print(sentence)

# 문자열 포매팅 - f-string 사용 (3.6 버전 이상)
name = "Lucky"
age = 43
sentence = f"My name is {name} and I'm {age} years old."
print(sentence)


