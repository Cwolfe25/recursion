def get_powers(number,additional):
    while additional >= 0:
        if additional == 0:
            return 1
        elif additional >0:
            return number*get_powers(number,additional-1) 
def get_compound_interest_balance(principal,rate,time):
    while time >= 0:
        if time == 0:
            return principal
        elif time > 0: 
            return (1 + rate) *  get_compound_interest_balance(principal,rate,time-1)
    
    
def main():
    print("1 = factorial 2 = summation 3 = powers 4 = sum of digits 5 = fibonacci 6 = GCD 7 = Euclids 8 = compound intrest 9 = product of 2 numbers 10 = square root")
    menu = input("what do you want to do?")
    
    if menu == "3":
        number = input("what is the number that is manipulated")
        additional = input("what is the amount of times you want this to repeat")
        number = int(number)
        additional = int(additional)
        get_powers(number,additional)
        print(number*get_powers(number,additional-1))
    elif menu == "8":
        principal = input("what is the innitial amount")
        rate = input("what is the rate")
        time = input("what is the amount of time")
        principal = int(principal)
        rate = float(rate)
        time = int(time)
        get_compound_interest_balance(principal,rate,time)
        
if __name__ == '__main__':
    main()