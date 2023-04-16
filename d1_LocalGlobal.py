gun=10

def checkpoint(soldiers): #경계근무
    global gun #전역 공간에 있는 gun 사용 이걸 넣어야지 위에 gun=10값을 사용함
    gun=gun-soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun=gun-soldiers #함수 내 지역변수
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun #반환하면 바뀜

print("전체 총: {0}".format(gun))
gun=checkpoint_ret(gun, 2)
print("남은 총: {0}".format(gun))