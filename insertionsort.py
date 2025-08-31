size=int(input("How many items do you want in the list?"))
l1=[]
for i in range(size):
    user=int(input("What do you want in the list?"))
    l1.append(user)
print(l1)
for i in range(1,size):
    key=l1[i]
    j=i-1
    while j>=0 and l1[j]>key:
        l1[j+1]=l1[j]
        j=j-1
    l1[j+1]=key
    print("after inserting",key,":",l1)
print("final",l1)
                                  