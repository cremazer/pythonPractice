# 반복문 for 예제
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80] # 성적 리스트
number = 0 # 학생 번호
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# for문과 continue
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

# for문과 함께 자주 사용하는 range 함수
a = range(10)
print(a) # range(0, 10)
a = range(1, 11)
print(a) # range(1, 11)

# range 함수를 이용한 1부터 10까지 더하기
add = 0
for i in range(1, 11):
    add = add + i
    print(add)

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print('')

# 리스트 내포 사용하기
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result) # [3, 6, 9, 12]

# 리스트 내포 사용하기
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result) # [3, 6, 9, 12]

# 리스트 내포 사용하기
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result) # [6, 12]

# 리스트 내포 사용하기
result = [x * y for x in range(2, 10)
          for y in range(1, 10)]
