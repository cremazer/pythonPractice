# 오류처리 실습

# f = open('non_existent_file.txt', 'r') # FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'

try:
    # 오류가 발생할 수 있는 코드
    f = open('non_existent_file.txt', 'r')
except FileNotFoundError as e:
    # 오류가 발생했을 때 실행할 코드
    print(e)
    print('파일이 존재하지 않습니다.')
else:
    # 오류가 발생하지 않았을 때 실행할 코드
    print('파일이 존재합니다.')
finally:
    # 오류 발생 여부와 상관없이 무조건 실행할 코드
    print('프로그램을 종료합니다.')
    f.close()

try:
    age = int(input('나이를 입력하세요: '))
except ValueError:
    print('숫자만 입력하세요.')
else:
    print(f'나이는 {age}세 입니다.')

# raise 예외 발생
try:
    raise NameError('예외 발생')
except NameError as e:
    print(e)

