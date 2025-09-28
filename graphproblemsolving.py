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
    #defining depth first search
    def dfs(self,start,visited=None):
        if visited is None:
            visited=set()
        visited.add(start)
        print(start,end=" ")
        for i in self.graph.get(start,[]):
            if i not in visited:
                self.dfs(i,visited)
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

#performing dfs

graph1.dfs("o")