from multiprocessing import Pool
from multiprocessing import Process

def f(x):
    return x*x

def ff(name):
    print('Hello', name)


if __name__ == '__main__':
    # with Pool(5) as p:
    #     print(p.map(f, [1,2,3]))

    p = Process(target=ff, args=('bob',))
    p.start()
    p.join()