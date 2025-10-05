#creating class graph
class graph:
    def __init__(self,v):
        self.v=v
        self.l1=[[] for i in range(v)]
    #func for dfs
    def dfs(self,temp,vertx,visted):
        visted[vertx]=True
        temp.append(vertx)
        for i in self.l1[vertx]:
            if visted[i]==False:
                temp=self.defs(temp,i,visted)
        return temp
    #func to add undirected edge
    def edge(self,vertx1,vertx2):
        self.l1[vertx1].append(vertx2)
        self.l1[vertx2].append(vertx1)
    def retrive(self):
        visited=[]
        connected=[]
        for i in range(self.vert):
            visited.append(False)
        for z in range(self.vert):
            if visited[z]==False:
                temp=[]
                connected.append(self.dfs(temp,z,visited))
        return connected
#mainfunc
if __name__=="__main__":
    var=graph(5)
    var.edge(1,2)
    var.edge(3,4)
    var.edge(4,5)
    print(var)
    #getting all the connecting variables
    connectedv=var.retrive()
    print("Connected components are: ")
    print(connectedv)
    


