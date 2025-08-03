#You are given a number n. Your task is to write a Python function that recursively 
# calculates the sum of the first n natural numbers.

def countdown(num):
    if num==1:
        return 1
    else:
        return num+countdown(num-1)
user=int(input("Give a starting number:"))
sum=countdown(user)
print(sum)
