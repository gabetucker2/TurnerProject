# LIBRARIES
import numpy as np

# SCRIPTS
import functions_helper

# FUNCTIONS

# summation function
def Σ(i, n, v):
    sum = 0
    for j in range(i, n + 1):
        sum += v(j)
    return sum

# expected reward(configuration)
def ER(c):
    return Σ(1, 5, lambda i: V(f(i, c(i))))

# softmax(configuration)
def P(c):
    numerator = np.exp(β*ER(c))
    denominator = 0
    return functions_helper.safeDivide(numerator, denominator, -9999999999999)
