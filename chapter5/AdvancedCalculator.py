from chapter5.Calculator import Calculator

# 상속 클래스는 다음과 같이 사용할 수 있음 : class 클래스명(상속받을 클래스명)
class AdvancedCalculator(Calculator):
    def pow(self, a, b):
        self.result = a ** b
        return self.result

    def div(self, a, b):
        if b == 0:
            return '0으로 나눌 수 없습니다.'
        else:
            self.result = a / b
            return self.result