def divisible_5(x):
    if x % 5 == 0:
        return True
    else:
        return False


def divisible_7(x):
    if x % 7 == 0:
        return True
    else:
        return False


def divisible_9(x):
    if x % 9 == 0:
        return True
    else:
        return False


def divisible_10(x):
    if x % 10 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    a=int(input("enter a number"))
    res=divisible_5(a)
    if res == True:
        print(res,"is divisible by 5")
    else:
        print(res,"not divisible")


    res2 = divisible_7(a)
    if res2 == True:
        print(res2, "is divisible by 5")
    else:
        print(res2, "not divisible")

    res3 = divisible_9(a)
    if res3 == True:
        print(res3, "is divisible by 5")
    else:
        print(res3, "not divisible")

    res4 = divisible_10(a)
    if res4 == True:
        print(res4, "is divisible by 5")
    else:
        print(res4, "not divisible")


