operation=input("Enter the operation with space in between : ")
opr=operation.split(" ")
op1=int(opr[0])
op2=int(opr[2])

def operator(op):
    switcher = {
        "+": op1+op2,
        "-": op1-op2,
        "*": op1*op2,
        "x": op1*op2,
        "/": op1/op2
    }
    return switcher.get(op, "Enter a valid operation")
print(operator(opr[1]))
 

