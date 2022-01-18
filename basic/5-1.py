import timeit
x = []
y = []
for strlen in range(10000,100001,10000):
    x.append(strlen)
    y.append(timeit.timeit("x==y[1:]",setup="strlen = {}; x = '1'*strlen; y = 'a'+'1'*strlen".format(strlen)))
    print(x[-1],y[-1])