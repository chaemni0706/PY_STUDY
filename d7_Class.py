top_name="윤태희"
top_age=26
top_bd=405

print("{0} 나례청 축역부 제1팀 수석 나자".format(top_name))
print("서류상 나이 {0}, 그럼 내 생일은 오늘로 해야겠다 {1}\n".format(top_age, top_bd))

bottom_name="김재겸"
bottom_age="200대 초반"
bottom_bd=1107

print("{0} 불로불사".format(bottom_name))
print("근데 친구는 몇 살이에요? {0}, 영원히 닳지 않는 목숨을 바쳐서 내가 널 이기게 해 줄게. {1}\n".format(bottom_age, bottom_bd))

def attack(top_name, location, bottom_name, a):
    print("{0}가 멱살을 잡고 {1}에서 {2}에게 {3}을 했다".format(top_name, location, bottom_name, a))

attack(top_name, "공원", bottom_name, "싸움")

