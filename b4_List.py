#리스트 []

#지하철 칸별로 10명, 20명, 30명

subway=["윤태희", "윤서주", "서윤건"]

print(subway)

#서윤건은 몇 번째 칸에 타고 있는가
print(subway.index("서윤건"))

#다음 정류장에서 서해영이 다음 칸에 탐
subway.append("서해영")
print(subway)

#고요한을 윤태희/윤서주 사이에 태우기
subway.insert(1, "고요한")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

subway.append("일레이")
print(subway)
print(subway.count("윤태희"))

#정렬
num_list=[5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
mix_list=[5,3,"여우경", True]
print(mix_list)

#리스트 확장
subway.extend(mix_list)
print(subway)