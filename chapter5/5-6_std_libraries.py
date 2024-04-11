# 표준 라이브러리 사용하기

import datetime
day1 = datetime.date(2024, 4, 11)
day2 = datetime.date(2024, 4, 18)
print(day1) # 2024-04-11
print(day2) # 2024-04-18

diff_day = day2 - day1
print(diff_day.days) # 7

# 시간 계산하기
import time
a = time.time()
for i in range(1, 1000):
    print("")

b = time.time()
print(b - a) # 실행시간을 출력한다

# sleep 함수 사용하기
for i in range(10):
    print(i)
    time.sleep(1) # 1초간 멈춘다