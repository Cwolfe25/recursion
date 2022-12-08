
def get_summation(n):
    if n == 0:
        return 0
    elif n > 0:
        return n + get_summation(n-1)

def get_sum_of_numbers_digits(n):
    if n == 10:
        return n
    elif n >= 10: 
        return get_sum_of_numbers_digits(n+10) + n / 10

def main():
    print(get_summation(5))

if __name__ == "__main__":
    main()

        