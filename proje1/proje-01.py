import moduller_01.hesapmaktry_01
import moduller_01.calender
import moduller_01.BMIhesaplama
import moduller_01.sıcaklıkhes
import moduller_01.cizimler
def anamenu():
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║   TTB APP           ║")
    print("║                     ║")
    print("║  1-Hesap makinesi   ║")
    print("║  2-Takvim           ║")
    print("║  3-BMI hesapla      ║")
    print("║  4-Sıcaklık çevirme ║")
    print("║  5-Çizimler         ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input ()
    if secim == "1" :
        moduller_01.hesapmaktry_01.hesaplarmenu()
        anamenu()
    if secim == "2" :
        moduller_01.calender.takvım()
        
    if secim == "3" :
        moduller_01.BMIhesaplama.BMI()
        
    if secim == "4" :
        moduller_01.sıcaklıkhes.sıcaklık()
        
    if secim == "5":
        moduller_01.cizimler.cizim()
        
ff = anamenu()
print(ff)

input()