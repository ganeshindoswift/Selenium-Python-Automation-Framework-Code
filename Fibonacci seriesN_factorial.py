"""Example of Recursive methords."""
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

factorial(5)
print(factorial(5))


# ************ Fibonacci series generation ************

def fbi(n):
    # if n==0:
    #     return 0
    # elif n==1:
    #     return 1
#     else:
#         return fbi(n-1) + fbi(n-2)

    f0, f1=0, 1
    fibbo=0
    if n==0:
        return 0
    else:
        for i in range(0, n):
            # print(fibbo, end="")
            f0=f1
            f1=fibbo
            fibbo=f0+f1
            print(fibbo, end="")
fbi(5)
