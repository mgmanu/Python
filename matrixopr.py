r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

A = []
B = []

print("Enter elements of Matrix A:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)

print("Enter elements of Matrix B:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    B.append(row)

result = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(0)
    result.append(row)

for i in range(r):
    for j in range(c):
        result[i][j] = A[i][j] + B[i][j]

print("Matrix Addition:")
for i in range(r):
    for j in range(c):
        print(result[i][j], end=" ")
    print()







r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

A = []
B = []

print("Enter elements of Matrix A:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)

print("Enter elements of Matrix B:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    B.append(row)

result = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Matrix Addition:")
for i in range(r):
    for j in range(c):
        print(result[i][j], end=" ")
    print()







result = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] - B[i][j])
    result.append(row)

print("Matrix Subtraction:")
for i in range(r):
    for j in range(c):
        print(result[i][j], end=" ")
    print()





























r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))

r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    A = []
    B = []

    print("Enter elements of Matrix A:")
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input()))
        A.append(row)

    print("Enter elements of Matrix B:")
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input()))
        B.append(row)

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

    print("Matrix Multiplication:")
    for i in range(r1):
        for j in range(c2):
            print(result[i][j], end=" ")
        print()










r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))

r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    A = []
    B = []

    print("Enter elements of Matrix A:")
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input()))
        A.append(row)

    print("Enter elements of Matrix B:")
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input()))
        B.append(row)

    result = []

    for i in range(r1):
        row = []
        for j in range(c2):
            sum = 0
            for k in range(c1):
                sum = sum + A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)

    print("Matrix Multiplication:")
    for i in range(r1):
        for j in range(c2):
            print(result[i][j], end=" ")
        print()

























r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

A = []

print("Enter elements of Matrix:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)

transpose = []
for i in range(c):
    row = []
    for j in range(r):
        row.append(0)
    transpose.append(row)

for i in range(r):
    for j in range(c):
        transpose[j][i] = A[i][j]

print("Transpose of Matrix:")
for i in range(c):
    for j in range(r):
        print(transpose[i][j], end=" ")
    print()













r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

A = []

print("Enter elements of Matrix:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)

transpose = []

for j in range(c):
    row = []
    for i in range(r):
        row.append(A[i][j])
    transpose.append(row)

print("Transpose of Matrix:")
for i in range(c):
    for j in range(r):
        print(transpose[i][j], end=" ")
    print()

















