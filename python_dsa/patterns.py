#patterns rules -> 
"""
1. the outer loop will be the number of lines (rows)
2. for the inner loop, focus on the columns, and connect them somehow to the lines (rows)
3. print the '*' inside the inner for loop
4. observe the symmetry [OPTIONAL] 
"""

def ptrn1(n):
    for i in range(n):
        for j in range(n):
            print('*', end=" ")
        print()


def ptrn2(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end=" ")
        print()

def ptrn3(n):
    for i in range(n):
        for j in range(1, i+2):
            print(j, end=" ")
        print()


def ptrn4(n):
    for i in range(n):
        for j in range(1, i+2):
            print(i+1, end=" ")
        print()

def ptrn5(n):
    for i in range(n):
        for j in range(n-i):
            print(" ", end=" ")
        for j in range((i+1)*2-1):
            print("*", end=" ")
        print()

def ptrn6(n):
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(1, n*2-(i*2)):
            print("*", end=" ")
        print()

def main():
    ptrn6(2)
    ptrn6(5)
    ptrn6(7)


if __name__=="__main__":
    main()
