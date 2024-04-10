# 파일 읽고 쓰기 연습
f = open("memo.txt", "w", encoding="UTF-8") # memo.txt 파일을 쓰기 모드로 열기
# f.write("Hello Python Programming...")
f.write("Hello Python 프로그래밍...")
f.close()

f = open("memo.txt", "r") # memo.txt 파일을 읽기 모드로 열기
data = f.read()
print(data)
f.close()

# with문을 사용하면 파일을 열고 닫는 것을 자동으로 처리
with open("memo.txt", "w") as f:
    f.write("Hello Python Programming...")

# 파일에 내용을 덧붙이기
with open("memo.txt", "a") as f:
    f.write("...and Data Science")

