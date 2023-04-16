cabinet={1:"윤태희", 3:"윤서주"}
print(cabinet[3])
print(cabinet[1])

print(cabinet.get(3))
print(cabinet.get(5)) #True
# print(cabinet(5)) 오류

print(cabinet.get(5, "사용가능"))
print(5 in cabinet) #False

cabinet={"a-1":"윤태희", "B-3":"윤서주"}
print(cabinet["a-1"])
print(cabinet["B-3"])

#새 손님
print(cabinet)
cabinet["C-20"]="서윤건"
cabinet["a-1"]="서해영"

print(cabinet)

#간 손님
del cabinet["a-1"]
print(cabinet)

#key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.values())

#목욕탕폐점
cabinet.clear()
print(cabinet)
