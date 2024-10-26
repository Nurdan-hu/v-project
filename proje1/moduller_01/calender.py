def takvım():
    import calendar
    year = int(input("Yılı giriniz: "))
    month = int(input("Ay giriniz: "))
    print(calendar.month(year,month))