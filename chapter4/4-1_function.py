# 함수 연습
def add(a, b): # a, b는 매개변수(또는 인자, 파라미터)
    return a + b

print(add(3, 4)) # 3, 4는 인수

# 입력값이 없는 함수
def say():
    return 'Hi'

print(say())

def sub(a, b):
    return a - b

print(sub(4, 2))

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul('add', 1, 2, 3, 4, 5))

print(add_mul('mul', 1, 2, 3, 4, 5))

def print_kwargs(**kwargs):
    # print(kwargs)
    print('a:', kwargs['a'])
    print('b:', kwargs['b'])

print_kwargs(a=1, b=2)

# 함수의 결과값은 언제나 하나
def add_and_mul(a, b):
    return a + b, a * b # 튜플로 반환

print(add_and_mul(3, 4))

# 매개변수 초기값 미리 설정
# 기본값이 지정된 매개변수는 항상 뒤쪽에 위치해야 함
def say_myself(name, old, man=True):
    print('나의 이름은 %s입니다.' % name)
    print('나이는 %d살입니다.' % old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('Lucky', 43)
say_myself('Lucky', 43, True)