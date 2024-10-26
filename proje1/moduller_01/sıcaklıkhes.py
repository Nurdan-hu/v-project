def sıcaklık():
    print("1- Celcius - Kelvin")
    print("2- Celcius - Fahrenheit")
    print("3- Kelvin - Celcius")
    print("4- Kelvin - Fahrenheit")
    print("5- Fahrenheit - Celcius")
    print("6- Fahrenheit - Kelvin")
    secim = (input("Hangisini seçtiniz?"))
    derece = float(input("Dereceyi giriniz:"))
    if secim == "1":
        print(derece + 273 , "K°")
    elif secim == "2":
        print(derece * 1.8 + 32 , "F°")
    elif secim == "3":
        print(derece-273 , "C°")
    elif secim == "4":
        print(1.8 * (derece - 273) + 32 , "F°")
    elif secim == "5":
        print((derece- 32) / 1.8 , "C°")
    elif secim == "6":
        print((derece+ 459.67)*5/9 , "K°")
  