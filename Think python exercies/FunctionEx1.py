# in this exersice I will implement functions, and call them within other functions

def repeat(string, n): # defining the repeat function
    print(string * n)    # this function will take in a string and output it n times
    

s = 'Spam, ' # declaring my string variable

def first_verse(): # declaring my first verse function
    repeat(s, 4)    # calling the repeat function, this function will ouput the string variable, 4 times, 
    repeat(s, 4)    # and 4 times again on a new line

def second_verse(): # declaring my second verse function that will repeat the string 2 times, then print (lovley spam, wonderful spam) then agian 2 times
    repeat(s, 2)    #calling my repeat function,
    print('(Lovley Spam, Wonderful Spam!)')
    repeat(s, 2)

def whole_verse(): # declaring my whole verse function that will print out the first two verses together
    first_verse() # calling the first verse function
    second_verse() #calling the second verse function

whole_verse() # calling my whole verse function



