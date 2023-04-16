#일반 혼불
class honbul:
    def __init__(toldju, name, age): #toldju=self
        toldju.name=name
        toldju.age=age
       
#상속 혼불        
class Attackhonbul(honbul):
    def __init__(toldju, name, age, bd): #toldju=self
        honbul.__init__(toldju, name, age)
        toldju.bd=bd
    
    def group(toldju, location):
        print("{0}, {1} 소속".format(toldju.name, location))

top=Attackhonbul("윤태희", 26, 405)
top.group("나례청 축역부 제 1팀")