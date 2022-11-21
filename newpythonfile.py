from generic_recursion import Get_Product_of_2_Whole_Numbers
from walker_recursive import get_factorial
from walker_recursive import get_fibonacci
from walker_recursive import get_GCD
from Generic_Recursion_dylan import get_summation
from Generic_Recursion_dylan import get_sum_of_numbers_digits
def get_powers(number,additional):
    '''
    takes additional and number
    returns number to the power of additional
    variables:
        additional = int
        number = int
    number is the number thats being exponeted 
    additional is the exponet 
    number to the additional power
    '''
    while additional >= 0:                                                                  #allows for the function to repeat
        if additional == 0:                                                                 #if the power is 0 it equals 1
            return 1
        elif additional >0:                                                                 #if the number is greater than zero then it runs the function again and subtracts additional until it gets to zero
            return number*get_powers(number,additional-1)                                   #basically this is saying that 2 to the fourth is equal to 2 time 2 to the third
def get_compound_interest_balance(principal,rate,time):
    '''
    takes prinicipal rate and time 
    returns compund intrest formula of the starting value times 1 + the rate to the power of time = the money made
    variables:
        principal = int
        rate = int
        time = int
    principal is the amount of money put into the intrest
    rate is the rate of the growth / decay in percentages 
    time is the amount of time the stock is growing
    '''
    
    while time >= 0:                                                                        #allows the function to repeat
        if time == 0:                                                                       #saying if it has been 0 amount of time then your money is what you put in 
            return principal
        elif time > 0:                                                                      #if its greater than zero it it subracts one time until it reaches zero
            return (1 + rate) *  get_compound_interest_balance(principal,rate,time-1)       #This uses the compund intrest formula of the starting value times 1 + the rate to the power of time = the money made

    
    
    
def main():
    print("1 = factorial 2 = summation 3 = powers 4 = sum of digits 5 = fibonacci 6 = compound intrest 7 = product of 2 numbers 8 = GCD")
    menu = input("what do you want to do?")
    
    if menu == "1":
        number = input("what number do you want factorialed")
        number = int(number)
        get_factorial(number)
        print(number * get_factorial(number - 1))
    elif menu == "2":
        n = input("what number do you want")
        n = int(n)
        get_summation(n)
        print(n + get_summation(n-1))
    elif menu == "3":
        number = input("what is the number that is manipulated")
        additional = input("what is the amount of times you want this to repeat")
        number = int(number)
        additional = int(additional)
        get_powers(number,additional)
        print(number*get_powers(number,additional-1))
    elif menu == "4":
        n = input("what number do you want")
        n = int(n)
        get_sum_of_numbers_digits(n)
        print(get_sum_of_numbers_digits(n+10) + n % 10)
    elif menu == "5":
        number = input("what number do you want to get fibonacci")
        number = int(number)
        get_fibonacci(number)
        print(get_fibonacci(number-1)+get_fibonacci(number-2))

    elif menu == "6":
        principal = input("what is the innitial amount")
        rate = input("what is the rate")
        time = input("what is the amount of time")
        principal = int(principal)
        rate = float(rate)
        time = int(time)
        get_compound_interest_balance(principal,rate,time)
        print((1 + rate) *  get_compound_interest_balance(principal,rate,time-1))
    elif menu == "7":
        a = input("what is the first number you want to multiply")
        b = input("what is the second number you want to multipy")
        a = int(a)
        b = int(b)
        Get_Product_of_2_Whole_Numbers(a,b)
        print(a + Get_Product_of_2_Whole_Numbers(a,b-1))
    elif menu == "8":
        first = input("what do you what the first number you want")
        first = int(first)
        constant1 = int(first)
        second = input("what is the other number that you want")
        get_GCD(constant1,first,second)
        print(get_GCD(constant1,first,second))

        
if __name__ == '__main__':
    main()