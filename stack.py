class stack():
    def __init__(self):
        self.l1=[]
    def push(self,items):
        self.l1.append(items)
        print(items,"push to stack")  
    def empty(self):
        if len(self.l1)==0:
            print("List is empty")
        else:
            print("List is not empty")
        return len(self.l1)==0
    def pop(self):
        if not self.empty():
            return self.l1.pop()
        else: 
            print("Stack is empty")
    def size(self):
        return len(self.l1)
    def display(self):
        print(self.l1)
#creating stack
s1=stack()
s1.push(67)
s1.push(41)
s1.push(10)
s1.display()
r=s1.empty()
print(r)