FibArray = [0,1]
 
def fibonacci(n):
    if n<=len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib

print(fibonacci(int(input())))