absent=[2, 5]
no_book=[7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in  no_book:
        print("stop. {0} follow me".format(student))
        break    
    print("{0}, read a book".format(student))
