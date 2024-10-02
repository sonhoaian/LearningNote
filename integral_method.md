# Several method to calculate an integral/integrations
In this section, I only mention to some highlighting methods as defined below:
1. **Trapezoidal Rule**: Approximates the integral by dividing the area under the curve into trapezoids and summing their areas.

2. **Simpson's Rule**: Uses parabolic segments to approximate the integral, providing a more accurate estimate than the trapezoidal rule for smooth functions.

3. **Midpoint Rule**: Evaluates the function at the midpoint of each interval and multiplies by the width of the intervals to estimate the area.

4. **Romberg Integration**: Combines the trapezoidal rule with Richardson extrapolation to improve accuracy.

5. **Gaussian Quadrature**: Uses strategically chosen points and weights to evaluate the integral, optimizing accuracy for polynomials of a certain degree.

6. **Monte Carlo Integration**: Uses random sampling to estimate the integral, particularly useful for high-dimensional integrals.

7. **Adaptive Quadrature**: Dynamically adjusts the interval sizes based on the function's behavior, allowing for more accurate results in areas where the function varies significantly.

8. **Clenshaw-Curtis Quadrature**: Combines cosine interpolation with the trapezoidal rule for integration over an interval, especially effective for smooth functions.

9. **Composite Rules**: Breaks the integral into smaller sections, applying methods like the trapezoidal or Simpson’s rule to each section and summing the results.

10. **Newton-Cotes Formulas**: A family of formulas that include the trapezoidal and Simpson's rules, using equally spaced points for approximation.

Then, we will work throught it in each subsections

## 1. Trapezoidal Rule
For the function f(x) is given, and an interval is devided in to **n** subsspaces with a step of **h**

$$h = \dfrac{a - b}{n}$$

so we have n space on an interval **(a, b)** that will have at least one solution on all subspaces on the interval. And the method will be present as

$$\int^{a}_{b} f(x) dx\approx  \frac{h}{2} \bigg[ f(a) + 2 \sum_{i=1}^{n-1} f(x_i) + f(b)  \bigg]$$

- The algorithm:
> 1. Choose the number of sub-intervals
> 2. Calculate the step **h**
> 3. Evaluate the function **f(x)** at two-end points 
> 4. Plug these values in to the Trapezoidal rule

and the algorithms is:

```plaintext
ALGORITHM TrapezoidalRule(f, a, b, n)
    INPUT: 
        f: function to integrate
        a: lower limit of integration
        b: upper limit of integration
        n: number of subintervals
    OUTPUT: 
        Approximate value of the integral

    h ← (b - a) / n              
    sum ← 0                      

    //calculate the values at both ends of a and b
    sum ← sum + f(a)             
    sum ← sum + f(b)             

    // the main iliteration to calculate
    FOR i FROM 1 TO n - 1 DO
        x_i ← a + i * h           
        sum ← sum + 2 * f(x_i)    
    END FOR

    result ← (h / 2) * sum        
    RETURN result                 
END ALGORITHM
```


base on these steps, we have a pesudo code

```plaintext
FUNCTION TrapezoidalRule(f, a, b, n)
    h ← (b - a) / n              
    sum ← 0                      

    // Calculate the area of the endpoints
    sum ← sum + f(a)            
    sum ← sum + f(b)            

    // Loop through each subinterval
    FOR i FROM 1 TO n - 1 DO
        x_i ← a + i * h          
        sum ← sum + 2 * f(x_i)   
    END FOR

    result ← (h / 2) * sum       
    RETURN result                
END FUNCTION
```

Now, we will implement it in python thon code

```py
# _, a, b, c is a dummies which must be place with your function, bounds, and specific number of subspaces
f = lambda x: _ 
lower_bound = a 
upper_bound = b
no_of_subspace = c

f_a = f(a)
f_b = f(b)

step = abs(b-a)/n

sum = 0

# main calculation
sum = sum + f_a + f_b # adding values at both ends

for i in range(1, n):
    x_i = lower_bound + i + step
    sum  = sum + 2*f(x_i)

sum = sum*h/2
```

if you want to be more concise, we will try to define a function:

```py
# _, a, b, c is a dummies which must be place with your function, bounds, and specific number of subspaces
f = lambda x: _ 
lower_bound = a 
upper_bound = b
no_of_subspace = c

def Trapezoidal(func, lower, upper, subspaces):
    f_a = func(lower)
    f_b = func(upper)

    step = abs(lower - upper)/subspaces

    sum = 0

    sum = sum + f_a + f_b
    x_i = lower_bound

    for i in range(1, n):
        x_i += step
        sum  = sum + 2*func(x_i)

    return sum = sum*h/2
```


