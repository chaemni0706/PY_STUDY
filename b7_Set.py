#중복 안 됨, 순서 없음
my_set={1, 2, 3, 3, 3}
print(my_set)

java={"윤태희", "윤서주", "서윤건"}
python=set(["윤태희", "서해영"])

#교집합(java, python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합(java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python)
print(java.union(python)) #순서 없음

#차집합(java를 할 줄 알지만 python은 할 줄 모르는 개발자)
print(java-python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("여우경")
print(python)

#java를 까먹음
java.remove("윤서주")
print(java)