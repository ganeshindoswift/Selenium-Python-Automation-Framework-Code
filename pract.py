def fibonac(n):

    n=int(input(" enter the value of positive no"))

    f0,f1= 0, 1
    fibbonac=0
    if n<0:
        print("enter prositive no")
    else:
        for i in range(0, n):
            print(fibbonac, end="")
            f0=f1
            f1=fibbonac6
            fibbonac=f0+f1
fibonac(5)