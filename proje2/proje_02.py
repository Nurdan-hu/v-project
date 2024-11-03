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
        a= open(f"rehber.txt","r")
        print(a)
        okunan = a.read()
        print(okunan)
        telrehberi()
    elif secim == "2":
        adsoyad = (input("Ad-Soyad Giriniz:"))
        telno= (input("Telefon Numarasını Giriniz:"))

        dosya = open("rehber.txt","a",encoding="utf-8")
        dosya.write ( "\n" +adsoyad + "-" + telno )
        print("Kayıt işlemi başarıyla gerçekleşmiştir.")
    elif secim == "3":
        pass
    elif secim == "4":
        pass
telrehberi()
input()