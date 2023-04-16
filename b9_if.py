weather=input("How's weather today?: ")
if weather=="rain" or weather=="snow":
    print("bring your umbrella")
elif weather=="dusk":
    print("bring your mask")
else:
    print("you don't need stuff")

temp=int(input("기온은 어때?: "))
if 30<temp:
    print("very hot")
elif 10<=temp and temp <30:
    print("good")
elif 0<=temp and temp<10:
    print("cold")
else:
    print("very cold")