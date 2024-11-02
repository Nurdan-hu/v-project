def Kisi():
    class Kisiler:
        def __init__(self,isim,soyad,numara):
            self.isim= isim
            self.soyad= soyad
            self.numara= numara
        def show_info(self):
            print(f"{self.isim} {self.soyad}    Numara:{self.numara} ")
        
    k1= Kisiler ("Annen","Tuğba",5555555555)
    k1.show_info()

    k2= Kisiler ("Baban","İsmail",5444444444)
    k2.show_info()

    k3= Kisiler ("Kardeşin","Zümra",5333333333)
    k3.show_info