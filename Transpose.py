r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix = []

for i in range(r):
    row = []
    for j in range(c):
        value = int(input("Enter element: "))
        row.append(value)
    matrix.append(row)

print("Original Matrix:")
for i in range(r):
    print(matrix[i])

transpose = []

for j in range(c):
    row = []
    for i in range(r):
        row.append(matrix[i][j])
    transpose.append(row)

print("Transpose Matrix:")
for i in range(c):
    print(transpose[i])