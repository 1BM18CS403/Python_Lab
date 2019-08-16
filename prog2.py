def fib(n):
     if n<=1:
            return n
     else:
         return(fib(n-1)+fib(n-2))

n=int(input("Enter the value of n : "))
if n<=0:
    print("Value cannot be negative")
else:
    print("fibonacci series : ")
    for i in range(n):
        print fib(i)
