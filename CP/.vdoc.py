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

    print(f"The result of f(x) = x^2 + 5 is {res: 5.5f}")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    step_len = 0.1
    y = 0 # initial value

    # Higher Order methods Function (2nd order)
    def Taylor2ndOrder(func, initial_val, lower, upper, distance):
        x0 = lower
        f_prime = sp.diff(func, x)
        y = initial_val

        while (x0 < upper):
            y = y + distance*func.subs(x, x0) + (distance**2/2)*f_prime, x0)
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
