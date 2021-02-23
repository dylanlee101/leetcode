import time
import functools
import cv2

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        res = func(*args,**kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__,end - start))
        return res
    return wrapper

@log_execution_time
def calculate_similarity(n):
    last = 0
    for i in range(n):
        last += i
    print(last)

if __name__ == '__main__':
    # calculate_similarity(10000)
    img = cv2.imread("")