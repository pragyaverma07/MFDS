r1 = int(input("Enter number of rows of first matrix: "))
c1 = int(input("Enter number of columns of first matrix: "))

A = []

print("Enter elements of first matrix:")
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    A.append(row)

r2 = int(input("Enter number of rows of second matrix: "))
c2 = int(input("Enter number of columns of second matrix: "))

B = []

print("Enter elements of second matrix:")
for i in range(r2):
    row = []
    for j in range(c2):
        row.append(int(input()))
    B.append(row)

if c1 != r2:
    print("Matrix multiplication is not possible.")
else:
    result = []

    for i in range(r1):
        row = []
        for j in range(c2):
            row.append(0)
        result.append(row)

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] = result[i][j] + A[i][k] * B[k][j]

    print("Resultant Matrix:")
    for i in range(r1):
        for j in range(c2):
            print(result[i][j], end=" ")
        print()