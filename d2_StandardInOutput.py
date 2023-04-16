import sys

print("py", "Java", "JavaScript", sep=", ", end="?") 
print("무엇이 더 재밌을까?")

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"math":0, "English":50, "coding":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") #왼쪽 정렬 8칸 확보, 오른쪽 정력 4칸 확보

#은행 대기 순번표
for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3)) #001, 002 ...

answer=input("아무 값이나 입력: ")
print(type(answer))
print("입력하신 값은" + answer + "입니다")
