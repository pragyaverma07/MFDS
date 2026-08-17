n = int(input("Enter the order of matrix: "))

matrix = []

print("Enter the elements row by row:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

def determinant(matrix, n):
    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0

    for j in range(n):
        submatrix = []

        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    row.append(matrix[i][k])
            submatrix.append(row)

        det = det + ((-1) ** j) * matrix[0][j] * determinant(submatrix, n - 1)

    return det

print("Determinant =", determinant(matrix, n))