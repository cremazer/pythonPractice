import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')

# sys.py를 실행할 때 다음과 같이 입력하면:
# python3 sys_upper.py a b c d
# A B C D 출력됨