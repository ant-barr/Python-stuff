# for these exersies there is a few more turtle functions:
# penup
# lifts the turtles imaginary pen so it doesnt leave a trail when it moves.
# pendown
# puts the pen back down

# the following function uses penup and pendown to move the turlte without leaving a trail

# %%
import math
from jupyturtle import make_turtle, penup, pendown, forward, left
# %%
def jump(length):
    """Move forward length units without leaving a trail.
    
    Postcondition: leaves the pen down.
    """
    penup()
    forward(length)
    pendown()

# Exercise 1
# write a function called rectangle that draws a rectangle with given side lengths.

# %%
def rectangle(W, H):
    forward(W)
    left(90)
    forward(H)
    left(90)
    forward(W)
    left(90)
    forward(H)
    left(90)

# %%
make_turtle()
rectangle(80, 40)
# %%

# Exercise 2
# write a function called rhombus that draws a rhobus with a given side length
# and a given interior angle:
def rhombus(length, n):
    forward(length)
    left(n)
    forward(length)
    left(180 - n)
    forward(length)
    left(n)
    forward(length)
    left(180 - n)

make_turtle()
rhombus(60, 40)
# %%
# Exercise 3
# Now write a more general function called parallelogram that draws
# a quadrilateral with parallel sides. Then rewrite rectangle and rhombus to use parallelogram.
def parallelogram(l, w, a):
    for i in range(2):
        forward(l)
        left(a)
        forward(w)
        left(180 - a)

make_turtle()
parallelogram(20, 40, 40)
# %%
# rewriting rectangle and rhombus to call parallelogram
def rectangle2(lengthR, widthR):
    parallelogram(l=lengthR, w=widthR, a=90)

make_turtle()
rectangle2(40, 50)
# %%
# rewriting rhombus
def rhombus2(lengthRh, n2):
    parallelogram(l=lengthRh, w=lengthRh, a=n2)

make_turtle()
rhombus2(40, 60)
# %%
# Exercise 4
# Write an appropriately general set of functions that can draw 3d shapes
# Hint, write a function called triangle that draws one triangular segment, 
# and then a function called draw_pie that uses triangle
def triangle(length, angle):
   base_angle = (180 - angle) / 2
   base_length = math.sin(angle/2*math.pi/180)*length*2
   forward(length)
   left(180-base_angle)
   forward(base_length)
   left(180-base_angle)
   forward(length)

make_turtle()
triangle(40, 45)

def draw_pie(segments, length):
    for i in range(segments):
        triangle(length, 360/segments)
        left(180)

make_turtle(delay=0.2)
draw_pie(5, 40)



# %%
# exersie 5
# make an appropriatley general set of functions that can draw flowers
# Hint: use arc to write a function called petal that draws one flower petal
"""
Arc length: L = 2πr * (angle / 360)
Arc ≈ n small lines → step length = L/n, step turn = angle/n
Petal = 2 arcs, mirrored with turn (180 - angle)
Flower = petals spaced evenly by 360/petals
"""

def polyline(n, length, angle):
    for i in range(n):
        forward(length)
        left(angle)



def arc(radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)


def petal(length, angle):
   for i in range(2):
       arc(length, angle)
       left(180-angle)

make_turtle(delay = 0)
petal(40, 60)

def draw_flower(petals, length, angle):
    for i in range(petals):
        petal(length, angle)
        left(360/petals)

make_turtle(delay = 0.000002)
draw_flower(20, 80, 45)


# %%
