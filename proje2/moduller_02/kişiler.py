def Kisi():
    class Kisiler:
        def __init__(self,isim,numara):
            self.isim= isim
            self.numara= numara
        def show_info(self):
            print(f"{self.isim}   Numara:{self.numara} ")
        
    k1= Kisiler ("Annen",5555555555)
    k1.show_info()

    k2= Kisiler ("Baban",5444444444)
    k2.show_info()

    k3= Kisiler ("Kardeşin",5333333333)
    k3.show_info()