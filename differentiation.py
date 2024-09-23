import math


def f(x):
    return math.sin(x)


h = 1e-10

for x in range(100):
    # 1) Calculate the limit definition of the derivative of f at x and store it in a variable
    lim = ((f(x+h) - f(x))/h)
    # 2) Print out the answer as "f'(INPUT) = OUTPUT" where INPUT is the value of x and OUTPUT is the limit rounded to two decimals.
    print(f"f'({x})={round(lim, 2)}")
