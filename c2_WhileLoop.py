'''
customer="윤태희"
index=5

while index>=1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
    index-=1

    if index==0:
        print("커피는 폐기처분 되었습니다.")

customer2="윤서주"
index2=1
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer2, index2))
    index2+=1 
'''
customer3="서윤건"
person="Unknown"

while person != customer3:
    print("{0}, 커피가 준비 되었습니다.".format(customer3))
    person=input("이름이 어떻게 되세요?: ")

    