class user():
    #hidden variable
    __Password="12345"
    def __init__(self,name,email,username):
        self.name=name
        self.email=email
        self.username=username
    def get_password(self):
        return self.__Password
    def set_password(self):
        oldpassword=input("Enter old password:")
        if oldpassword==self.__Password:
            newpassword=input("Give a new password:")
            self.__Password=newpassword
        else:
            print("Password is incorrect")
#obj creation
obj1=user("Randitya","randitya@gmail.com","Randitya_8")
print(obj1.name)
print(obj1.get_password())
obj1.set_password()
print(obj1.get_password())