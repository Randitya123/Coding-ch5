Elements=int(input("How many elements do you want?"))
l1=[]
for i in range(Elements):
    Elementss=int(input("what elements do you want?(ascending order)"))
    l1.append(Elementss)
find=int(input("What element are you tying to find?"))
firstindex=0
lastindex=Elements-1
found=False
while firstindex<=lastindex:
    middleindex=(firstindex+lastindex)//2
    if l1[middleindex]==find:
        print("Element was found ",middleindex)
        found=True
        break
    elif l1[middleindex]<find:
        firstindex=middleindex+1
    else:
        lastindex=middleindex-1
if found==False:
    print("Element not found")
    


    


