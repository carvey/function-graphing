from .tools import register_function
import math

# @register_function("Linear")
def linear(x):
    return 1000 * x

@register_function("Quadratic")
def quadratic(x):
    return pow(x, 2)

@register_function("Cubic")
def cubic(x):
    return pow(x, 3) * .001

@register_function("Quadratic Polynomial")
def polynomial(x):
    return (
            pow(x, 2) + (300 * x) + 15000
    ) * 0.7604562737642585

@register_function("Logarithmic")
def logarithmic(x):
    if x > 0:
        return math.log(x) * 144764.82730108395
