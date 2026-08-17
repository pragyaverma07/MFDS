r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))

print("Enter first matrix:")
a=[]

for i in range(r):
    row=[]
    for j in range(c):
        x=int(input())
        row.append(x)
    a.append(row)

print("Enter second matrix:")
b=[]

for i in range(r):
    row=[]
    for j in range(c):
        x=int(input())
        row.append(x)
    b.append(row)

result=[]
for i in range(r):
    row=[]
    for j in range(c):
        row.append(a[i][j]+b[i][j])
    result.append(row)

print("Resultant matrix:")

for i in range(r):
    for j in range(c):
        print(result[i][j],end=" ")
    print()