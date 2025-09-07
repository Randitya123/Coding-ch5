size=int(input("How big do you want the list to be?"))
l1=[]
for i in range(size):
    user=int(input("What do you want in the list?"))
    l1.append(user)
print(l1)
size2=1
while size2<size:
    l2=[]
    for i in range(0,size,2*size2):
        #if i+1<size:
            leftstart=l1[i:i+size2]
            rightstart=l1[i+size2:i+2*size2]
            l3=[]
            a,b=0,0
            #merging
            while a<len(leftstart)and b<len(rightstart):
                if leftstart[a]<rightstart[b]:
                    l3.append(leftstart[a])
                    a+=1
                else:
                    l3.append(rightstart[b])
                    b+=1
            #add remainign elemant
            while a<len(leftstart):
                l3.append(leftstart[a])
                a+=1
            while b<len(rightstart):
                l3.append(rightstart[b])
                b+=1
            l2.extend(l3)
    l1=l2
    size2*=2
print(l1)


                


