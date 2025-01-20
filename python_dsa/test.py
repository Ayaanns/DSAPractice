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
        for j in range(n-i):
            print(" ", end=" ")
        for j in range(2*i-1):
            print("*", end=" ")
        print()
    # print() 
    for i in range(n):
        # UP TRIANGLE
        for j in range(i):
            print(" ", end=" ")
        for j in range(2*n-(2*i+1)):
            print("*", end=" ")
        print()

def ptrn3(n):
    for i in range(2*n):
        start = i
        if i >= n: start = 2*n-i
        for _ in range(start):
            print("*", end=" ")
        print()


def ptrn4(n):
    for i in range(1, n+1):
        for _ in range(n-i):
            print("-", end=" ")
        letter = ord('A')
        for j in range(2*i-2):
            print(chr(letter), end=" ")
            if j<=(2*i)/2: letter+=1
            else: letter-=3
        print()
    # for i in range(1, n+1):
        # if i%2==0: counter = 1
        # else: counter = 0


    



#def ptrn1(n):
# ptrn(4)
ptrn4(4)
            
