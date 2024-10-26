def BMI():
    kütle = float(input("Kilonuzu giriniz -kilogram-: "))
    boy = float (input("Boyunuzu giriniz -metre- :"))
    BMI = (kütle/(boy*boy))
    print(BMI)
    if BMI < 18.5 :
        print("İdeal kilonun altındasınız.") 
    elif BMI < 24.9 and BMI > 18.5:
        print("İdeal kilodasınız.")
    elif BMI > 25:
        print("İdeal kilonun üstündesiniz.")