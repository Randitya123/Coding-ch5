size=int(input("How big do you want the list to be?"))
l1=[]
for i in range(size):
    user=int(input("What do you want in the list?"))
    l1.append(user)
print(l1)
size2=1
while size>1:
    l2=[]
    for i in range(0,size,2):
        if i+1<size:
            leftstart=l1[i]
            rightstart=l1[i+1]
            l3=[]
            a,b=0,0
            #merging
            while a<len[leftstart] and b<len[rightstart]
