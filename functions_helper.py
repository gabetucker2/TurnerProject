# FUNCTIONS

def safeDivide(numerator, denominator, failCase):
    if denominator == 0:
        return failCase
    else:
        return numerator / denominator
