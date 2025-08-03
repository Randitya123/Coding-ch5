#You are given a number n. 
# Your task is to write a Python function that uses recursion to calculate the factorial of n.
# The factorial of a number is the product of all positive integers from 1 to n.
def fac(num):
    if num==1 or num==0:
        return 1
    else:
        return num*fac(num-1)
user=int(input("Give number:"))
dt=fac(user)
print(dt)