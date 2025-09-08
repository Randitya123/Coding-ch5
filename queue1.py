class queue():
    def __init__(self):
        self.l1=[]
    def enqueue(self,item):
        self.l1.append(item)
        print(item,"enqueued to queue")
    def empty(self):
        if len(self.l1)==0:
            print("List is empty")
        else:
            print("List is not empty")
        return len(self.l1)==0
    def size(self):
        return len(self.l1)
    def display(self):
        print(self.l1)
    def dequeue(self):
        if not self.empty():
            index=self.l1[0]
            self.l1.remove(index)
        else:
            print("queue is empty")
    def peek(self):
        if not self.empty():
            index=self.l1[0]
            print("Front of the queue is", index)
        else:
            print("Queue is empty")
            
        

