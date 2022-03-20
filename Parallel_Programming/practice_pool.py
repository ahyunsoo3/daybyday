from multiprocessing import Process, Value, Array
# from multiprocessing import Process, Pipe
#
# def f(conn):
#     conn.send([42, None, 'Hello'])
#     conn.close()
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())
#     p.join()

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num,arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])

    