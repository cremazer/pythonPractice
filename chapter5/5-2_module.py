# 모듈 연습
# 모듈은 함수나 변수 또는 클래스를 모아 놓은 파일이다.
from modules import CommonUtil

# 모듈 안의 함수만을 가져와서 사용할 수 있다.
from modules.CommonUtil import lower


print(CommonUtil.upper('python')) # PYTHON
print(lower('PYTHON')) # python

