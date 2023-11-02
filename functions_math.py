# LIBRARIES
import numpy as np

# SCRIPTS
import parameters
import functions_helper

# FUNCTIONS

# summation function
def Σ(v, f):
    sum = 0
    for i in v:
        sum += f(i)
    return sum

# for c, c' = all possible c values except current c value
def nPrime(val, vec):
    return [e for e in vec if e != val]

# expected reward(configuration)
def ER(c):
    return Σ(range(1, 5+1), lambda i: V(f(i, c(i))))

# softmax(configuration)
def P(c):
    numerator = np.exp(β*ER(c))
    denominator = Σ(nPrime(c, parameters.C), lambda cPrime: np.exp(β*ER(cPrime)))
    return functions_helper.safeDivide(numerator, denominator, -9999999999999)

def V(t, f, i, j):
    if t >= 1:
        if j == s[i,t]:
            return V(t-1, f[i,j]) + η(r[t] - ER(c[t])) # todo: check syntax
        else: # j != s[i,t]
            return parameters.d * V(t-1, f[i,j]) # TODO: figure out of f[i,j] is proper syntax
    else:
        return 0
