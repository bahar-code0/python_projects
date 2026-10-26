n = int(input("Enter the number of rows for Pascal's Triangle: "))

for i in range(n):
    for j in range(n - i):
        print(" ", end="")
    coef = 1
    for j in range(i + 1):
        print(coef, end=" ")
        coef = coef *(i - j) // (j + 1)
    print()
