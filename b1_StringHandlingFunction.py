py="Python is Amazing"
print(py.lower())
print(py.upper())
print(py[0].isupper())
print(len(py))
print(py.replace("Python", "Java"))

index=py.index("n")
print(index)

index=py.index("n", index+1)
print(index)

print(py.find("n"))

print(py.find("Java")) 

print(py.count("n"))