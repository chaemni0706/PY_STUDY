score_file=open("score.txt", "w", encoding="utf8")
print("math: 0", file=score_file)
print("engilsh: 50", file=score_file)
score_file.close()

score_file=open("score.txt", "a", encoding="utf8")
score_file.write("science: 80")
score_file.write("\ncoding: 100")

# score_file=open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file=open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file.close()

score_file=open("score.txt", "r", encoding="utf8")
while True:
    line=score_file.readline()
    if not line:
        break
    print(line)
score_file.close()


score_file=open("score.txt", "r", encoding="utf8")
lines=score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()