class User():
    def __init__(self,username, password,email):
        self.username=username
        self.password=password
        self.email=email






class UserRepository():
    def __init__(self):
        self.users=[]
        self.isLoggedIn= False
        self.currentUser ={}
        # UYGULAMA ÜZERİNDEKİ BİLGİLERİ .JSON ÜZERİNDEN ALMA
        self.loadUser()
    def loadUser(self):
        pass

    def register(self, user : User):

        self.users.append(User)
        #self.savetoFile()
        print("Kullanıcı Oluşturuldu")

    def login(self):
        pass
    def savetoFile(self):
        pass



repository=UserRepository()

while True:
    print("Menü".center(50,"*"))
    secim=input("1 -Register\n2 -Login\n3 - Logout\n4 -İdentity\n5 - Exit\nseçiminiz: ")
    if secim==5:
        break
    else:
        if secim==1:
            username=input("username: ")
            password=input("password: ")
            email=input("email: ")

            user =User(username=username, password = password, email=email)
            print(repository.register(user))
        elif secim==2:
            pass #login
        elif secim==3:
            pass #logout
        elif secim==4:
            pass #display username
        else:
            print("Yanlış seçim")

