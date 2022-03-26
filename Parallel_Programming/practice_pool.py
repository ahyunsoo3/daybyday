from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1,2,3]))

# offers both local and remote concurrency.
# It runs on both Unix and Windows.
# The above example demonstrates the common practice of defining such functions
# Therefore, child processes can successfully import that module.

# Reference : https://docs.python.org/3/library/multiprocessing.html