Terms=int(input("How many terms do you want?"))
def fib(num):
    if num<=1:
        return num
    else:
        return fib(num-1)+fib(num-2)
for i in range(Terms):
    print(fib(i),end=" ")
