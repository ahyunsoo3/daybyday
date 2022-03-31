class Test(object):

    def __getitem__(self, tt):
        print (type(tt), tt)


test = Test()
test[5]
test[5:65:5]
test['GEEKS']
test[1, 'x', 10.0]


#
# a, b = 4, 7
#
# c = a.__add__(b)
#
#
# print(c)

# Reference : https://www.geeksforgeeks.org/__getitem__-in-python/#:~:text=__getitem__()%20is%20a%20magic,getitem__(x%2C%20i)%20.
