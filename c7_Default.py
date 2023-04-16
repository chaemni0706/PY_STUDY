# def profile(name, age, main_lang):
#     print("name: {0}\tage:{1}\tmain_lang:{2}".format(name, age, main_lang))

# profile("윤태희", 28, "파이썬")
# profile("윤서주", 20, "자바")

def profile(name, age=20, main_lang="파이썬"):
    print("name: {0}\tage:{1}\tmain_lang:{2}".format(name, age, main_lang))

profile("고요한")
profile("윤서주")