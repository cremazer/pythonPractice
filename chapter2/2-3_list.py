# 리스트 선언
odd = [1, 3, 5, 7, 9]
print(odd)
print(type(odd))

# 리스트에 문자와 숫자를 함께 넣기
a = [1, 2, 'Life', 'is']
print(a)

# 리스트에 리스트 넣기
b = [1, 2, ['Life', 'is']]
print(b)

# 리스트 인덱싱 -> 0부터 시작
c = [1, 2, 3]
print(c[0]) # 1 출력
print(c[1] + c[2]) # 5 출력

# 리스트 슬라이싱
d = [1, 2, 3, 4, 5]
print(d[0:2]) # [1, 2] 출력

# 리스트 연산
e = [1, 2, 3]
f = [4, 5, 6]
print(e + f) # [1, 2, 3, 4, 5, 6] 출력

# 리스트 반복
g = [1, 2, 3]
print(g * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3] 출력

# 리스트 길이 구하기
h = [1, 2, 3]
print(len(h)) # 3 출력

# 리스트 수정
i = [1, 2, 3]
i[2] = 4
print(i) # [1, 2, 4] 출력

# 숫자와 문자 연산
print('hi' + '3') # TypeError: can only concatenate str (not "int") to str

# 리스트 삭제
j = [1, 2, 3]
del j[1]
print(j) # [1, 3] 출력

# 리스트에 요소 추가
k = [1, 2, 3]
k.append(4)
print(k) # [1, 2, 3, 4] 출력

# 리스트 정렬
l = [1, 3, 4, 2]
l.sort()
print(l) # [1, 2, 3, 4] 출력

# 리스트 뒤집기
m = [1, 3, 4, 2]
m.reverse()
print(m) # [2, 4, 3, 1] 출력

# 위치 반환
n = [1, 2, 3]
print(n.index(3)) # 2 출력

# 리스트에 요소 삽입
o = [1, 2, 3]
o.insert(0, 4)
print(o) # [4, 1, 2, 3] 출력

# 리스트 요소 제거
p = [1, 2, 3, 1, 2, 3]
p.remove(3)
print(p) # [1, 2, 1, 2, 3] 출력

# 리스트 요소 끄집어내기
q = [1, 2, 3]
print(q.pop()) # 3 출력
print(q) # [1, 2] 출력

# 리스트에 포함된 요소 x의 개수 세기
r = [1, 2, 3, 1]
print(r.count(1)) # 2 출력

# 리스트 확장
s = [1, 2, 3]
s.extend([4, 5])
print(s) # [1, 2, 3, 4, 5] 출력