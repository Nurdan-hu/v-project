def cizim():
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║   TTB APP           ║")
    print("║                     ║")
    print("║  1-Daire            ║")
    print("║  2-Üçgen            ║")
    print("║  3-Kare             ║") 
    print("║  4-Beşgen           ║") 
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim= input()
    import turtle
    if secim =="1":
        ok = turtle.Turtle()

        ok.circle(150) #yarı çapı 150 olan bir çember çizer

        turtle.done()
    if secim == "2":
        kalem=turtle.Turtle()
        kalem.pencolor("red")
        kalem.pensize(5)
        for i in range(3):
            kalem.forward(200)
            kalem.left(120)
        turtle.done()
    if secim == "3":
        for a in range (4):
            turtle.speed(10)
            turtle.forward(100)
            turtle.right(90)
        turtle.done()
    if secim == "4":
        kalem=turtle.Turtle()
    kalem.pencolor("blue")
    kalem.pensize(5)
    for i in range(5):
        kalem.forward(200)
        kalem.left(72)