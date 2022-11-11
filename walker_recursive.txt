'''
author: @wlaitala
created: 11/7/22
updated: 11/7/22

description: Collection of various recursive functions
bugs: None obviously
'''
def main():
    number = "24,10"
    number = number.split(",")
    first = int(number[0])
    constant1 = int(number[0])
    #constant2 = int(number[1])
    second = int(number[1])
    print(get_GCD(constant1,first,second))
def get_factorial(number):                                  #define the function for factorial
    '''
    description:
        finds the factorial of the input. Formula is N * (N-1)!. If return ever gets to 0, returns 1
    Arguments:
        number: input number, integer, 1
    Takes:
        input from user, is a positive integer or zero
    Returns:
        A positive nonzero integer, is the factorial of the input
    '''
    while 0 <= number:                                      #loops for "number" many times
       if number == 0:                                      #if the number variable is equal to zero,
            return 1                                        #return 1
       elif number > 0:                                     #But if the number variable is greater than zero,
            return number * get_factorial(number-1)         #return the number variable times the factorial of number minus one

def get_fibonacci(number):                                  #define the function for number
    '''
    description:
        finds the Xth number in the fibonacci sequence, where X is the number the user inputs. Formula is F(n-1) + F(n-1). If return is ever 1 or 0, return 1 or 0, respectively
    Arguments:
        number: the input of the user, integer, 1
    Takes:
        input from user, is a positive integer
    Returns:
        An integer that is a number of the fibonacci sequence
    '''
    if number == 0:                                         #if number is equal to zero,
        return(0)                                           #return zero
    elif number == 1:                                       #else if number is equal to zero,
        return(1)                                           #return one
    else:                                                   #if number if anything else
        return(get_fibonacci(number-1)+get_fibonacci(number-2)) #return the previous two numbers in the sequence, added together
def get_GCD(constant1,first,second):
    '''
    description:
        finds the greatest common divisor of two numbers determined by the user. Tests every number between number #1 and zero, and sees if they are divisors of both input numbers. Test starting at number #1 and goes down, so the first hit will be the GCD
    Arguments:
        constant1: the first number they inputted
        first: The everchanging variable that is every number between constant1 and 0
        second: The second number they inputted
    Takes:
        two positive integers from the user
    Returns:
        an integer that is a positive integer
    '''
    if constant1 % first == 0:                              #tests every number between their first number and zero, if the remainder is 0 (that means it is a divisor), it sends to another if statement
        if second % first == 0:                             #If the number that has been proven to be a factor of their first input is also a factor of their second number, it is the greatest common divisor.
                                                            #ABOVE CONTINUED...Because it is tested greatest to least, the first one that is a factor of both has to be the GCD 
            return first                                    #Returns the number that is being tested
        else:                                               #if the number that is being tested is a divisor of number #1 but not of number #2
            return(get_GCD(constant1,first-1,second))       #Run it again except test for one number lower
    else:                                                   #If the number being tested is not a factor of number #1
        return(get_GCD(constant1,first-1,second))           #Run again but test for a number one lower
main()