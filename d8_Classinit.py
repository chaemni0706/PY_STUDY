class honbul:
    def __init__(toldju, name, age, bd): #toldju=self
        toldju.name=name
        toldju.age=age
        toldju.bd=bd
        print("{0} 나례청 축역부 제1팀".format(toldju.name))
        print("근데 친구는 몇 살이에요? {0}, 그영원히 닳지 않는 목숨을 바쳐서 내가 널 이기게 해 줄게. {1}\n".format(toldju.age, toldju.bd))
        
top=honbul("윤태희", 26, 405)
bottom=honbul("김재겸", "200대  초반", 1107)
