# 클래스 연습하기
from chapter5.Calculator import Calculator
from chapter5.AdvancedCalculator import AdvancedCalculator
from chapter5.Cookie import Cookie
from chapter5.Family import Family

cal = Calculator()
print(cal.add(3, 4))

cookie = Cookie('choco', 'cookie')
print(cookie.__getitem__(0))
print(cookie.__str__())

# 상속 클래스 사용하기
advanced_cal = AdvancedCalculator()
print(advanced_cal.add(3, 4)) # 7
print(advanced_cal.pow(3, 4)) # 81
print(advanced_cal.div(3, 4)) # 0.75
print(advanced_cal.div(3, 0)) # 0으로 나눌 수 없습니다.

family = Family("Lucky")
print(family.__str__()) # Family with Lucky
