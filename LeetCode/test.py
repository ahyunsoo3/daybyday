def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i


myg = create_generator()
print(myg)

for i in myg:
    print(i)