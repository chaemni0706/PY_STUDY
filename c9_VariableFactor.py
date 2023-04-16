def profile(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("윤서주", 20, "Python", "Java", "c", "c++", "c#", "JavaScript")
profile("고요한", 22, "Kotlin", "Swift", "", "", "")