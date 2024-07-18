cols=int(input("Enter the number of columns in the 2D matrix: "))
rows=int(input("Enter the number of rows in the 2D matrix: "))
print(f"Enter {rows*cols} numbers")
matrix=[]
for i in range(0,rows):
    mat=[]
    for j in range(0,cols):
        mat.append(int(input()))
    matrix.append(mat)
print("Matrix:")
for i in range(0,rows):
    for j in range(0,cols):
        print(matrix[i][j],end=" ")
    print()
transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Transpose:")
for i in range(0,rows):
    for j in range(0,cols):
        print(transposed[i][j],end=" ")
    print()
