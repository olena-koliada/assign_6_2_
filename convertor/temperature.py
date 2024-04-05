# temperature module should implement two functions of converting
# Celsius to Fahrenheit and vice versa, as we don't know which way
# we'll need to convert.

# You may use these formulas:

# C=(5/9)(F−32)
# °F = (°C x 9/5) + 32

# Derive the formula for another direction.

# Fahrenheit grad converting to Celsius grad


def temperature_c(f):
    c = (5 / 9) * (int(f) - int(32))
    return float(c)

# Celsius grad converting to Fahrenheit grad


def temperature_f(c):
    f = (9 * c + 160) / 5
    return float(f)

# check print result
# print(temperature_f(9))
# print(temperature_c(22))
