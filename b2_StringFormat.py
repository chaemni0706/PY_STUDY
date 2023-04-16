#print("a"+"b")
#print("a", "b")

#1
print("나는 %d살입니다." %20)
print("나는 %s를 좋아해요." %"코코")
print("Apple은 %c로 시작해요." %"A")

print("나는 %s색과 %s색을 좋아해요." %("분홍", "보라"))

#2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("핑크", "보라"))
print("나는 {0}색과 {1}색을 좋아해요.".format("핑크", "보라"))
print("나는 {1}색과 {0}색을 좋아해요.".format("핑크","보라"))

#3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=21, color="분홍"))

#4
age2=21
color2="pink"

print(f"나는 {age2}살이며, {color2}색을 좋아해요.")
