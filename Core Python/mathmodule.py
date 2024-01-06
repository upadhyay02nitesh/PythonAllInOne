import math

# Basic Arithmetic
x = 5.6
y = -2.3
print("Ceiling of", x, "is:", math.ceil(x))
print("Floor of", y, "is:", math.floor(y))
print("Truncated value of", y, "is:", math.trunc(y))

# Exponential and Logarithmic Functions
print("e^", x, "is:", math.exp(x))
print("Natural logarithm of", x, "is:", math.log(x))
print("Base-10 logarithm of", x, "is:", math.log10(x))

# Trigonometric Functions
angle_degrees = 45
angle_radians = math.radians(angle_degrees)
print("Sine of", angle_degrees, "degrees is:", math.sin(angle_radians))
print("Cosine of", angle_degrees, "degrees is:", math.cos(angle_radians))
print("Tangent of", angle_degrees, "degrees is:", math.tan(angle_radians))

# Hyperbolic Functions
print("Hyperbolic sine of", x, "is:", math.sinh(x))
print("Hyperbolic cosine of", x, "is:", math.cosh(x))
print("Hyperbolic tangent of", x, "is:", math.tanh(x))

# Power and Root Functions
power_result = math.pow(2, 3)
print("2^3 is:", power_result)
print("Square root of", x, "is:", math.sqrt(x))

# Constants
print("The value of pi is:", math.pi)
print("The value of e is:", math.e)

# Angular Conversion
print("45 degrees in radians is:", math.radians(45))
print("π/4 radians in degrees is:", math.degrees(math.pi/4))

# Other Functions
print("Absolute value of", y, "is:", math.fabs(y))
print("Factorial of 5 is:", math.factorial(5))

# Modf Function
fractional, integer = math.modf(x)
print("Fractional part of", x, "is:", fractional)
print("Integer part of", x, "is:", integer)

a=-10
print(abs(a))