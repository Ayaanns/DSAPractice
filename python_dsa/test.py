def ptrn(n):
    for i in range(2*n):
        start = i
        if i <= n: print("*"*(i+1))
        if i >= n: 
            start = 2*n-i
            print("*"*start)


def ptrn1(n):
    for i in range(n):
        # DOWN TRIANGLE
        for j in range(n-i+1):
            print(" ", end=" ")
        for j in range(2*i):
            print("*", end=" ")
        print()
    # print() 
    # for i in range(n):
    #     # UP TRIANGLE
    #     for j in range(i):
    #         print(" ", end=" ")
    #     for j in range(2*n-(2*i)):
    #         print("*", end=" ")
    #     print()



#def ptrn1(n):
# ptrn(4)
ptrn1(4)
            
