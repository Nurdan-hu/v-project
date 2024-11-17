def kisi_listele():
        try:
            dosya = open("rehber.txt","r")
            kisiler= dosya.readlines()
            for c, b in enumerate(kisiler, start= 1):
                  print(c,b)
        except:
            print("Dosya bulunamadı")
                
            
            
            
def kisi_ekle():
        adsoyad = (input("Ad-Soyad Giriniz:"))
        telno= (input("Telefon Numarasını Giriniz:"))
        dosya = open("rehber.txt","a",encoding="utf-8")
        dosya.write (adsoyad + "-" + telno )
        print("Kayıt işlemi başarıyla gerçekleşmiştir.")
        
    
def rehber_sil():
    print("Mevcut kayıtlar")
    kisi_listele()
    silinecek = int(input ("Hangi kayıt silinecek(numarasını girin):"))
    dosya = open("rehber.txt","r+",encoding="utf-8")
    okunan = dosya.readlines()
    silinecekKayit = okunan[silinecek]
    print("Silinecek kayıt : ", silinecekKayit)
    dosya.close()

    dosya = open("rehber.txt","w")    
    for a in okunan:
        if a != silinecekKayit: dosya.write(a)
    dosya.close()  
            
def kisi_düzenleme():
    print("Mevcut kayıtlar")
    kisi_listele()
    duzeltilecek = int(input ("Düzeltilecek kayıtın kaçıncı olduğunu giriniz:"))
    dosya = open("rehber.txt","r+",encoding="utf-8")    
    okunan = dosya.readlines()
    duzeltilecekKayit = okunan[duzeltilecek]
    print("Düzeltilecek kayıt : ", duzeltilecekKayit)
    dosya.close()

    dosya = open("rehber.txt","w")    
    for a in okunan:
        if a == duzeltilecekKayit: 
            print("\n\n Yeni bilgileri giriniz:")
            ad  = input("Ad  : ")
            tel = input("Tel : ")
            dosya.write(f"{ad}-{tel}\n")
        else: dosya.write(a)

    dosya.close()

def telrehberi():
    print("╔═════════════════════╗")
    print("║  Telefon Rehberi    ║")
    print("║                     ║")
    print("║  1-Kişilerim        ║")
    print("║  2-Kişi Ekleme      ║")
    print("║  3-Kişi Silme       ║")
    print("║  4-Kişi Düzenleme   ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()

    if secim == "1": 
        kisi_listele()
        telrehberi()
    if secim == "2" : 
        kisi_ekle()
        telrehberi()
    if secim == "3" : 
        rehber_sil()
        telrehberi()
    if secim == "4" : 
        kisi_düzenleme()
        telrehberi()
telrehberi()
input()