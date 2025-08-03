#countdown
def countdown(num):
    '''if num==0:
        print("END")
    else:'''
    print(num)
    num=num-1
    countdown(num)
firstnum=int(input("What number do you want to start with?"))
countdown(firstnum)

