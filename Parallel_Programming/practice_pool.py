import time

def sleepy_man():
    print('Starting to sleep')
    time.sleep(3)
    print('Done sleeping')

tic = time.time()
sleepy_man()
sleepy_man()
toc = time.time()

print('Done in {:.4f} second'.format(toc-tic))








# Refernce : https://www.analyticsvidhya.com/blog/2021/04/a-beginners-guide-to-multi-processing-in-python/