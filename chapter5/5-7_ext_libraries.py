# 외부 라이브러리 사용하기
# 설치 예 : pip3 install requests (requests 최신 버전 라이브러리 설치)
# 라이브러리 검색 : https://pypi.org/

# 최신 버전 업그레이드
# pip3 install --upgrade requests

# 설치된 라이브러리 목록 보기
# pip3 list

# Faker 라이브러리 사용하기
# 라이브러리 사용법은 https://faker.readthedocs.io/en/master/ 참고
# 구글링 검색 : python faker
# Chat GPT를 활용한다.
# 설치 : pip3 install Faker

from faker import Faker
# fake = Faker()
fake = Faker('ko_KR')
print(fake.name())
print(fake.address())
print(fake.text())
