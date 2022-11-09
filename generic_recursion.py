def P(a,b):
    if b > 0:
        return a + P(a,b-1)
    elif b == 0:
        return 0


if __name__ == "__main__":
    print(P(7,4))