import moduller_02.kişiler
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
        moduller_02.kişiler.Kisi()
        telrehberi()