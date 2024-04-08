# 조건문 연습
money = True # True, False 중 하나의 값을 가질 수 있음, 소문자는 사용 불가능
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

x = 3
y = 2
print(x > y) # True
print(x < y) # False
print(x == y) # False
print(x != y) # True

# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어 가라
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# 만약 3000원 이상의 돈을 가지고 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어 가라
money = 2000
card = True
if money >= 3000 or card: # or는 소문자만 사용 가능
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# 포함 연산자 in
print(1 in [1, 2, 3]) # True
print(1 not in [1, 2, 3]) # False

# 튜플에서 포함 연산자 in 사용
print('a' in ('a', 'b', 'c')) # True
print('j' not in ('a', 'b', 'c')) # True

# 공백도 문자열로 인식
print('p ' in 'python') # False
print('p' in 'python') # True

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# pass 사용
pocket = ['paper', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

# 다중 조건 판단 elif : else if의 줄임말
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

