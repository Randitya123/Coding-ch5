#defning the graph class
class Graph():
    def __init__(self):
        self.graph={}
    def nodes(self,item):
        if item not in self.graph:
            self.graph[item]=[]
    #func to add edge between 2 nodes
    def edge(self,item1,item2,direct=False):
        if item1 not in self.graph:
            self.nodes(item1)
        if item2 not in self.graph:
            self.nodes(item2)
        self.graph[item1].append(item2)
        if not direct:
            self.graph[item2].append(item1)
    def display(self):
        for i in self.graph:
            print(f"{i}: {self.graph[i]}")
    def deletenode(self,item):
        if item in self.graph:
            for i in self.graph:
                if item in self.graph[i]:
                    self.graph[i].remove(item)
            #deleting the node
            del self.graph[item]
        else:
            print("Item doesnt exist")
    def deleteedge(self,item1,item2,direct=False):
        if item1 in self.graph and item2 in self.graph[item1]:
            self.graph[item1].remove(item2)
        else:
            print("item doesnt exist")


        
graph1=Graph()
graph1.nodes("i")
graph1.nodes("a")
graph1.nodes("f")
graph1.nodes("j")
graph1.nodes("v")
graph1.nodes("g")
graph1.nodes("m")
graph1.nodes("t")
graph1.nodes("o")
graph1.nodes("r")

#adding edges between nodes
graph1.edge("i","a")
graph1.edge("a","f")
graph1.edge("f","j")
graph1.edge("j","v")
graph1.edge("v","g")
graph1.edge("g","m")
graph1.edge("m","t")
graph1.edge("t","o")
graph1.edge("o","r")
graph1.edge("i","r")


#calling the display func
graph1.display()

#deleting edge
graph1.deleteedge("m","t")
print("Graph after deleting m and t: ")
graph1.display()

#deleting node
graph1.deletenode("o")
print("Graph after deleting node (o): ")
graph1.display()
