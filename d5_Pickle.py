import pickle
# profile_file=open("profile.pickle", "wb")
# profile={"name":"윤태희", "age": 28, "hobby":["reading", "exercise", "김재겸"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

profile_file=open("profile.pickle", "rb")
profile=pickle.load(profile_file)
print(profile)
profile_file.close()