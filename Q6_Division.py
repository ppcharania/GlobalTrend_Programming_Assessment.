def div_num(a, b):
    try:
        result = a/b
        rem=a%b
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"

a=int(input("Enter dividend: "))
b=int(input("Enter divisor: "))
print(div_num(a,b))  

