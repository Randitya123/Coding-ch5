class user():
    __marks="Randitya"
    def __init__(self,name,schoolclass,subject):
        self.name=name
        self.schoolclass=schoolclass
        self.subject=subject
    def get_result(self):
        return self.__marks
    def set_marks(self):
        namepassword=input("Enter code:")
        if namepassword==self.__marks:
            tests=input("You got 92/100 in math")
            self.__marks=tests
        else:
            print("Code is incorrect")
#obj creation
obj1=user("Randitya","8RN","Math")
print(obj1.name)
print(obj1.schoolclass)
print(obj1.subject)
obj1.set_marks()
print(obj1.get_result())