# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def EulerMethod(func, lower, upper, seed, step):
    x = lower
    y = seed

    # length of step
    step_len = abs(lower - upper)/step

    # Loop and take sum of function values
    for i in range(step):
        # update the result
        y = y + step_len*func(x, y)

        # re-assign x
        x += step_len

    return y
#
#
#
#
#
#
#
def EulerMethod(func, seed, lower, upper, step):
    x = lower
    y = seed

    # Loop and take sum of function values
    while x <= upper:
        # update the result
        y = y + step*func(x)

        # re-assign x
        x = x + step

    return y

f = lambda x: x**2 + 5
a = 2
b = 4
stp = 0.001
int_val = 0.0

res = EulerMethod(f, int_val, a, b, stp)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import sympy as sp

# declare function
x = sp.symbols('x')
f = x**2 + 5

f_prime = sp.diff(f, x)

# declare variable for calculation
a = 2
b = 4
step_len = 0.001
y = 0 # initial value

# Higher Order methods Function (2nd order)
def Taylor2ndOrder(func, initial_val, lower, upper, distance):
    x0 = lower
    f_prime = sp.diff(func, x)
    y = initial_val

    while (x0 <= upper):
        y = y + distance*func.subs(x, x0) + (distance**2/2)*f_prime.subs(x, x0)
        x0 += distance

    return y

res = Taylor2ndOrder(f, y, a, b, step_len)
print(res)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def MidPoint(func, initial_val, lower, upper, deltaX):
    
    x = lower
    y = initial_val

    while(x <= upper):
        y = y + deltaX*func(x + deltaX/2, y + (deltaX/2)*func(x, y))
        x += deltaX

    return y
#
#
#
#
#
#
f = lambda x, y = 1: y + x**2 + 5
a = 2
b = 4
y = 9
step_len = 0.0001

def MidPoint(func, initial_val, lower, upper, deltaX):
    
    x = lower
    y = initial_val
    z = 0

    while(x <= upper):
        y = y + deltaX*func(x + deltaX/2, y + (deltaX/2)*func(x, y))
        x += deltaX
        z += y*deltaX
    return y

res = MidPoint(f, y, a, b, step_len)
print(res)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def EulerEnhaced(func, initial_val, lower, upper, deltaX):

    # Assign local variable
    y = initial_val
    x = lower

    while (x <= upper):
        y = y + (deltaX /2)* (func(x, y) + func(x + deltaX, y + deltaX*func(x, y)))
        x += deltaX

    return y
#
#
#
#
#
#
#
f = lambda x, y = 1: y + x**2 + 5

init_val = 9
a = 2
b = 4
step_len = 0.0001

def EulerEnhaced(func, initial_val, lower, upper, deltaX):

    # Assign local variable
    y = initial_val
    x = lower

    while (x <= upper):
        y = y + (deltaX /2)* (func(x, y) + func(x + deltaX, y + deltaX*func(x, y)))
        x += deltaX

    return y

res = EulerEnhaced(f, init_val, a, b, step_len)
print(res)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def RungeKutta3(func, initial_val, lower, upper, deltaX):

    x = lower
    y = initial_val

    while (x <= upper):

        k1 = deltaX*func(x, y)

        k2 = deltaX*func(x + deltaX / 3, y + k1 / 3)

        k3 = deltaX*func(x + (deltaX * 2) / 3, y + (k2 * 2) / 3)

        y = y + (k1 + 3 * k3) / 4

        x += deltaX
    
    return y
#
#
#
#
#
f = lambda x, y = 1: y + x**2 + 5

init_val = 9
a = 2
b = 4
step_len = 0.0001

def RungeKutta3(func, initial_val, lower, upper, deltaX):

    x = lower
    y = initial_val

    while (x <= upper):

        k1 = deltaX*func(x, y)

        k2 = deltaX*func(x + deltaX / 3, y + k1 / 3)

        k3 = deltaX*func(x + (deltaX * 2) / 3, y + (k2 * 2) / 3)

        y = y + (k1 + 3 * k3) / 4

        x += deltaX
    
    return y

res = RungeKutta3(f, init_val, a, b, step_len)

print(res)
```
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def RungeKutta4(func, init_val, lower, upper, deltaX):

    x = lower
    y = init_val

    while (x < upper):
        # Calculate number of RK4 
        k1 = deltaX * func(x, y)
        k2 = deltaX * func(x + (1/2) * deltaX, y + (1/2) * k1 * deltaX)
        k3 = deltaX * func(x + (1/2) * deltaX, y + (1/2) * k2 * deltaX)
        k4 = deltaX * func(x + deltaX, y + k3 * deltaX)
        
        y = y + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + deltaX

    return y
#
#
#
#
#

#
#
#
