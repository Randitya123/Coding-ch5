class tree():
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None
def inorder(root):
    if root.leftnode!=None:
        inorder(root.leftnode)
    print(root.data)
    if root.rightnode!=None:
        inorder(root.rightnode)
def inseett(root,item):
    if root==None:
        return tree(item)
    if root.data>item:
        root.leftnode=inseett(root.leftnode,item)
    else:
        root.rightnode=inseett(root.rightnode,item)
    return root
#function to find inorder successor
def inordersuccessor(root):
    current=root
    while current.leftnode is not None:
        current=current.leftnode
    return current
#function to delete a node
def delete(root,key):
    if root is None:
        return root
    if key<root.data:
        root.leftnode=delete(root.leftnode,key)
    elif key>root.data:
        root.rightnode=delete(root.rightnode,key)
    else:
        if root.leftnode is None:
            temp=root.rightnode
            root=None
            return temp
        #root has onkly left child
        elif root.rightnode is None:
            temp=root.leftnode
            root=None
            return temp
        else:
            temp=inordersuccessor(root.rightnode)
            print(temp.data)
            root.data=temp.data
            root.rightnode=delete(root.rightnode,temp.data)
    return root
#taking user input for creating tree
numofele=(int(input("Enter the number of elements: ")))
root=None
#adding each item
for i in range(numofele):
    nodes=int(input("enter the node value: "))
    root=inseett(root,nodes)
#inorder traversal
inorder(root)
#print("\n")
#case 1
leaf=int(input("enter leaf value to be deleted: "))
root=delete(root,leaf)
inorder(root)
#case 2 
child=int(input("enter the node with one child: "))
root=delete(root,child)
inorder(root)
#case3
child2=int(input("enter the node with two children: "))
root=delete(root,child2)
inorder(root)



