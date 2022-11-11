def Get_Product_of_2_Whole_Numbers(a,b):
    if b > 0:
        return a + Get_Product_of_2_Whole_Numbers(a,b-1)
    elif b == 0:
        return 0


if __name__ == "__main__":
    print(Get_Product_of_2_Whole_Numbers(7,4))