import time,functools

def log_time(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        t1 = time.time()
        r = func(*args,**kw)
        print('%s excute in %s ms:' % (func.__name__,1000*(time.time()-t1)))
        return r
    return wrapper
@log_time
def now():
    print("2020")

@log_time
def multi(x,y):
    return x * y

if __name__ == '__main__':
    now()
    print(multi(2,3))