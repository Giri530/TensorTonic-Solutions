from math import pi, sin, cos
def cyclic_encoding(values, period):
    return [[sin(2*pi*v/period),cos(2*pi*v/period)] for v in values]
    