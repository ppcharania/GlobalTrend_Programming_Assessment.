def nth_fibo(n):
    if n==1 or n==2:
        return n-1
    else:
        return (nth_fibo(n-1)+ nth_fibo(n-2))
n=int(input("Enter n: "))
res=nth_fibo(n)
print(res)
        
        
        
    
