
# these are the exercies from chapter 2
import math

# part 1
# The volume of a sphere with radius r is 4/3pir^3. what is the volume of a sphere with radius 5? 
# start with a variable named radius and then assign the result to a variable named volume.
# display the result, 
# add comments to indicate that radius is in centimeters and volume is in cubic centemeters

radius = 5 #cm

volume = (4/3) * math.pi * radius ** 3 # cm^3
volume2 = (4/3) * math.pi * math.pow(radius, 3) # using the built in exponentiatoin feature in the math module

print(round(volume, 1), 'cm^3')
print(round(volume2, 1), 'cm^3')

print(" ") # new line

# part 2
# A rule of trigonometry says that for any value of x,
# (cosx)2 + (sinx)2 = 1. 
# lets see if for a sepcified x value like 42.
# create a variable named x with this value. then use math.cos and math.sin to compute the sin
# and cosine of x, and the sum of their squares.
# the result should be close to 1.

x = 42

result = math.cos(x)**2 + math.sin(x)**2
print(result)

print(" ") ## new line

# part 3
# in addition to pi, the other variable defined in the math module is e, which represents the base of the 
# natural logarithm, written in math notation as e.
# now lets compute e^2 three ways

# 1. use math.e and the exponentiation operator (**).
method1 = math.e**2
print(method1)

# 2. use math.pow to raise math.e to the power 2.
method2 = math.pow(math.e, 2)
print(method2)

# use math.exp, which takes as an argument a value, x and computes e^x.
method3 = math.exp(2)
print(method3)

# why is method 3 slightly different form the other two, its seems to just be rounded a bit.
# the most accurate is method 3 because the other two rely on the stored approximation of math.e 15-16 digits

# outputs

# 523.6 cm^3
# 523.6 cm^3

# 1.0

# 7.3890560989306495
# 7.3890560989306495
# 7.38905609893065


