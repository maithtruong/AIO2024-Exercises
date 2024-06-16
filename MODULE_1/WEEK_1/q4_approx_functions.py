'''
    4. Approximate geometric functions.
'''

import math

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative values.")
    return 1 if n == 0 else n * factorial(n - 1)

def sin_approx(x, n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError(f"{n} must be a positive integer.")
    
    sin_x = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sin_x += term
    return sin_x

def cos_approx(x, n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError(f"{n} must be a positive integer.")
    
    cos_x = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        cos_x += term
    return cos_x

def sinh_approx(x, n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")
    
    sinh_x = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sinh_x += term
    return sinh_x

def cosh_approx(x, n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")
    
    cosh_x = 0
    for i in range(n):
        term = (x ** (2 * i)) / factorial(2 * i)
        cosh_x += term
    return cosh_x

def main():
    # Example
    x = 3.14
    n = 10
    
    print(f"approx_sin(x={x}, n={n}) = {sin_approx(x, n)}")
    print(f"approx_cos(x={x}, n={n}) = {cos_approx(x, n)}")
    print(f"approx_sinh(x={x}, n={n}) = {sinh_approx(x, n)}")
    print(f"approx_cosh(x={x}, n={n}) = {cosh_approx(x, n)}")

if __name__ == "__main__":
    main()