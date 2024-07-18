import time
import logging

logging.basicConfig(level=logging.INFO)

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper

@time_logger
def nth_fibo(n):
    if n==1 or n==2:
        return n-1
    else:
        return (nth_fibo(n-1)+ nth_fibo(n-2))
    
n=int(input("Enter n: "))
res=nth_fibo(n)
print(res)

        
        
        
    



