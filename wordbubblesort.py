size=int(input("How big do you want the list to be?"))
l1=[]
for i in range(size):
    items=str(input("what item do you want"))
    l1.append(items)
print(l1)

#bubblesort
for i in range(size-1):
    for j in range(0,size-1):
        if l1[j]>l1[j+1]:
            temp=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=temp
print(l1)

