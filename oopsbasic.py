#creating a class
class cars:
    def __init__(self,brand,color,electricity,miles):
        self.brand=brand
        self.color=color
        self.electricity=electricity
        self.miles=miles
    def get_color(self):
        return self.color
    def set_color(self ,newclr):
        self.color=newclr
#object creation
obj1=cars("Tesla","white",True,5000)
obj2=cars("BMW","Black",False,25000)
#printing attributes
print(obj1.color)    
print(obj2.miles)
#getting and setting the color
obj2.set_color("blue")
obj2.get_color()
print(obj2.color)