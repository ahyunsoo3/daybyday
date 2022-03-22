from multiprocessing import Process, freeze_support

def f():
    print('hlo wrold')

if __name__ == '__main__':
    freeze_support()
    Process(target=f).start()




#m : assert count == len(arr1) * arr1.itemsize

