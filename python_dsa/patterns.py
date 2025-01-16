#patterns rules -> 
"""
1. the outer loop will be the number of lines (rows)
2. for the inner loop, focus on the columns, and connect them somehow to the lines (rows)
3. print the '*' inside the inner for loop
4. observe the symmetry [OPTIONAL] 
"""

class YTPatterns:
    def __init__(self, n):
        """initialize the pattern printer with size n."""
        self.n = n

    def ptrn1(self):
        """print the square pattern of start"""
        for i in range(self.n):
            for j in range(self.n):
                print("*", end=" ")
            print()
        print() #EXTRA LINE BETWEEN PATTERNS

    def ptrn2(self):
        for i in range(self.n):
            for j in range(self.n-i):
                print("*", end=" ")
            print()
        print()




def print_test_case(n, pattern_num):
    """print a single test case with size n and specifiend patterns"""
    print(f"Test Caes: N= {n}, pattern {pattern_num}")
    print("-" * 40)
    pattern = YTPatterns(n)
    pattern_method = getattr(pattern, f"ptrn1")
    pattern_method()


def main():
    #list of test caess (Size, pattern_number)
    test_cases = [
        (2, 1), (5, 1), (7, 1),  # Pattern 1 with different sizes
        (2, 2), (5, 2), (7, 2),  # Pattern 2 with different sizes
        (2, 3), (5, 3), (7, 3),  # Pattern 3 with different sizes
        (2, 4), (5, 4), (7, 4),  # Pattern 4 with different sizes
        (2, 5), (5, 5), (7, 5),  # Pattern 5 with different sizes
        (2, 6), (5, 6), (7, 6),  # Pattern 6 with different sizes
        (2, 7), (5, 7), (7, 7),  # Pattern 7 with different sizes
    ]

    #run all test cases
    for size, pattern in test_cases:
        print_test_case(size, pattern)


def interactive_main():
    """interactive mode for running specified test cases"""
    while True:
        try:
            size = int(input("Enter the size (or 0 to exit): "))
            if size == 0:
                break
            pattern = int(input("ENter the pattern number (1-7): "))
            if not 1 <= pattern <= 7:
                print("Pattern number must be between 1 and 7")
                continue
            print_test_case(size, pattern)
        except ValueError:
            print("Please enter valid numbers")
        except Exception as e:
            print(f"An error occured: {e}")



if __name__=="__main__":
    mode = input("Choose mode (1 for automated test cases, 2 for interactive): ")
    if mode == "1":
        main()
    elif mode == "2":
        interactive_main()
    else:
        print("Invalide mode selected")
















