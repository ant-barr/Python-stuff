# Excersise 1
# in this exercise I will write a function called print_right that takes a string named text as an input parameter
# it will print the string with enough spaces tht the last letter of the string is in the 40th column of the display.

# Hint use the len function, the string concatenation operator (+), and the string repetition operator

def print_right(text):  # declare the function and take add the input parameter
    length = len(text)  # create a new variable that will store the length of the given text
    space = 40 - length # create another variable thit will store 40 - the length of the given text
    print(" " * space + text)  # print " " times the space variable (40 minus length) and concatenate the text

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")

# outputs
#                                   Monty
#                                Python's
#                           Flying Circus

# Exercise 2
# Write a function called triange that takes a string and an integer and draws
# a triangle with the given height, made up of copies of the string

def triangle(text, n): # declare the function with input parameters text and n for the string and the height
    for i in range(n + 1): # create a for loop that will iterate from i to n + 1 (because it starts from 0)
        print(text * i)   # print out the text times i, each loop will incrament i one time and will end with n+1

triangle('L', 5)

# outputs
# L
# LL
# LLL
# LLLL
# LLLLL

print() # space
# Exercise 3
# write a function called rectangle that takes a string and two integers and draws a rectangle with the given width and height
# made up of copies of the string.

def rectangle(text, w, h): # declare the rectangle functions with input parameters text, w, h
    for i in range (h):   # create a for loop that iterates h times (here we dont need h + 1 because we are not manipulating h,
        print((text * w))  # print text * W on each line of the iteration.
        

rectangle("H", 5, 4)

# outputs
# HHHHH
# HHHHH
# HHHHH
# HHHHH

print() # add space for the next exercise
# Exercise 4
# The song "99 Bottles of Beer" starts with this verse:
#   99 bottles of beer on the wall, 
#   99 bottles of beer.
#   Take one down pass it around,
#   98 bottles of beer on the wall.

# then the second verse is the same except that it starts with 98 bottles and ends with 97.
# the song continues - for a very long time - until there are 0 bottles of beer

# write a function called bottle_verse that takes a number as a parameter and displays the verse taht starts with 
# a given number of bottles.

# Hint start with a function that can print the first, second or last line of the verse, and use it to write bottle_verse.

def bottle_verse_first(n):
    for i in range(n, 0, -1):
        print( n ,"bottles of beer on the wall")
        print(n ,"bottles of beer")
        print("Take one down, pass it around")
        print(n - 1 ,"bottles of beer on the wall")
        print()
        n = n - 1

bottle_verse_first(99)