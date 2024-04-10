# 사용자 입출력 예제
a = input()

print("유저가 입력한 것:" + a)

# 프롬프트를 띄워 사용자 입력 받기
number = input("숫자를 입력하세요: ")
print(number)

# print함수로 두 개 이상의 값 출력
a = 123
b = 'python'
print(a, b) # 콤마로 연결한 파라미터는 띄어쓰기로 구분되어 출력한다.

# 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ') # end=' '는 print함수가 끝날 때 다음 줄로 넘어가지 않고 공백을 출력한다.