import math


def f(x):
    return x**2


a = 0
b = 100

DELTA = 1e-5

result = 0  # This variable will hold the resulting riemann sum that we're building
# This variable will hold the current point between a and b that we're evaluating
curr = a + DELTA
while curr <= (b+DELTA):

    # 1) Update result by adding the area created from a rectangle with width DELTA and height f(curr)
    result = result + DELTA*f(curr)
    # 2) Update curr to move past the point we just evaluated
    curr = curr+DELTA

# 3) Print out the answer as "integral(f, VA -> VB) = OUTPUT" where VA (and VB) is the value of a (and b) and OUTPUT is the sum rounded to two decimals.
print(f"integral(f, {a}-> {b})= {round(result, 4)}")
