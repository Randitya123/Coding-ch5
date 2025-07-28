class car():
    def __init__(self,brand,color,fuel,model):
        self.brand=brand
        self.color=color
        self.fuel=fuel
        self.model=model
    def get_color(self):
        return self.color
    def set_color(self,clr):
        self.color=clr
    def detail(self):
        print("Car - {} - {}, Fuel Type - {}, Color - {}".format(self.brand,self.model,self.fuel,self.color))
class suv(car):
    def __init__(self, brand, color, fuel, model,transmission,turbo):
        car.__init__(self,brand, color, fuel, model)
        self.transmission=transmission
        self.turbo=turbo
    def detail(self):
        print("Car - {} - {}, Fuel Type - {}, Color - {},Transmission - {},Turbo - {}".format(self.brand,self.model,self.fuel,self.color,self.transmission,self.turbo))

#object crteation
obj1=suv("Audi","Red","Diesel","R8","Automatic",True)
print(obj1.get_color())
obj1.detail()
obj1.set_color("White")
print(obj1.get_color())
obj1.detail()