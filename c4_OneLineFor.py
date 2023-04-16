#num 1, 2, 3, 4+front add 100-> 101 102 103

students=[1, 2, 3, 4, 5]
print(students)
students=[i+100 for i in students]
print(students)

#name->length
students=["윤태희", "일레이 리그로우", "서주희수"]
students=[len(i) for i in students]
print(students)

#name->NAME
students=["taehui", "seoju"]
students=[i.upper() for i in students]
print(students)