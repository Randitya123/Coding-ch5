import os
#func for printing folder structure
def explore(path,level=0):
    if not os.path.exists(path):
        print("folder does not exist")
        return
    items=os.listdir(path)
    for i in items:
        item=os.path.join(path,i)
        print(" " * level + "|--" + i)
        if os.path.isdir(item):
            explore(item,level+1)
#func to find a file
def search(path,file,cpath=None):
    if cpath is None:
        cpath=[path]
    if not os.path.exists(path):
        print("folder does not exist")
        return None
    for i in os.listdir(path):
        itempath=os.path.join(path,i)
        if i==file:
            return os.path.join(*cpath,i)
        
        if os.path.isdir(itempath):
            result=search(itempath,file,cpath+[i])
            if result:
                return result
    return None


if __name__=="__main__":
    folderpath=r"C:\Users\KIKE\OneDrive\Desktop"
    print("===== File Tree =====")
    explore(folderpath)
    #searching for the file\
    dt=str(input("Enter the file name to search:"))
    filepath=search(folderpath,dt)
    if filepath:
        print(f"File found at: {filepath}")
    else:
        print("File path was not found")
        