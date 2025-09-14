class tree():
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None

#Inorder traversing(LEFT - ROOT - RIGHT)
def inorder(root):
    if root.leftnode!=None:
        inorder(root.leftnode)
    print(root.data)
    if root.rightnode!=None:
        inorder(root.rightnode)
#func for inserting an item
def inseett(root,item):
    if root==None:
        return tree(item)
    if root.data>item:
        root.leftnode=inseett(root.leftnode,item)
    else:
        root.rightnode=inseett(root.rightnode,item)
    return root
def search(root,item2):
    if root.data==item2:
        return root
    elif root.data>item2 and root.leftnode!=None:
        return search(root.leftnode,item2)
    elif root.data<item2 and root.rightnode!=None:
        return search(root.rightnode,item2)
    else:
        return-1
    

#asking user input the numbre of items
user=int(input("Enter the number of items for the tree"))
root=None
for i in range(user):
    users=int(input("Enter the value of the node"))
    root=inseett(root,users)
inorder(root)

userss=int(input("Enter the node that you want to search for"))
node=search(root,userss)

if node==-1:
    print("Node does not exist")
else:
    print("node found",node.data)





