import math

def f(x):
    return x * math.log(x) - 16.0

def fprime(x):
    return 1.0 + math.log(x)

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    for i in range(0,MAX_ITER):
        x_1 = x_0 - f(x_0)/fprime(x_0)
        if (abs(x_0-x_1)<=EPSILON):
            return x_1
        x_0 = x_1
    return x_1