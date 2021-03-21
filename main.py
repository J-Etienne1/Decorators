
"""
def f1(func):
    def wrapper(*args, **kwargs):
        print('Started')
        val = func(*args, **kwargs)
        print('Ended')
        return val

    return wrapper
@f1
def f(a, b = 9):
    print(a,b)


f('Hi')



@f1
def add(x, y):
    return x+y

print(add(4,5))
"""

# Example 1
"""
import time
def before_after(func):
    def wrapper(*args):
        print('Before')
        func(*args)
        print('After')
    return wrapper

class Test:
    @before_after
    def decorated_method(self):
        print('run')

t = Test()
t.decorated_method()
"""


# Example 2
"""
import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print('Function took: ', time.time() - before, 'seconds')
    return wrapper

@timer
def run():
    time.sleep(2)

run()
"""


# Example 3

import datetime

def log(func):
    def wrapper(*args, **kwargs):
        with open('logs.txt', 'a') as f:
            f.write('Called function with ' + ' '.join([str(arg) for arg in args]) + ' at ' + str(datetime.datetime.now()) + '\n')
        val = func(*args, **kwargs)
        return val

    return wrapper

@log
def run(a,b,c=9):
    print(a+b+c)

run(1,3,c=9)





















