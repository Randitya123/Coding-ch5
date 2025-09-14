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


#preorder traversal(ROOT - LEFT - RIGHT)
def preorder(root):
    print(root.data)
    if root.leftnode!=None:
        inorder(root.leftnode)
    if root.rightnode!=None:
        inorder(root.rightnode)


#postorder traversal(LEFT - RIGHT - ROOT)
def postorder(root):
    if root.leftnode!=None:
        inorder(root.leftnode)
    if root.rightnode!=None:
        inorder(root.rightnode)
    print(root.data)


#obj creation
root=tree(6)    
root.leftnode=tree(5)
root.leftnode.leftnode=tree(4)
root.leftnode.leftnode.leftnode=tree(3)
root.leftnode.leftnode.leftnode.leftnode=tree(2)
root.leftnode.leftnode.leftnode.leftnode.leftnode=tree(1)

root.rightnode=tree(7)
root.rightnode.rightnode=tree(8)
root.rightnode.rightnode.rightnode=tree(9)
root.rightnode.rightnode.rightnode.rightnode=tree(10)
root.rightnode.rightnode.rightnode.rightnode.rightnode=tree(11)

inorder(root)

preorder(root)

postorder(root)