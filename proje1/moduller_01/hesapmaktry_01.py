def hesaplarmenu():
    print('     HESAP MAKİNESİ           ')
        
    print('     1- Toplama               ')      
    print('     2- Çarpma                ')
    print('     3- Çıkarma               ') 
    print('     4- Bölme                 ')
    
    secim = input()
    print(secim,'seçtiniz')
    if secim == '1':
        print('Toplama yapılacak...')
    if secim == '2':
        print('Çarpma yapılacak...')
    if secim == '3':
        print('Çıkarma yapılacak...')
    if secim == '4':
        print ('Bölme yapılacak...')
    num1 = float(input('Birinci sayıyı giriniz:' ))
    num2 = float(input('İkinci sayıyı giriniz:'))
    if secim == '1':
        print(num1+num2)
    if secim == '2':
        print (num1*num2)
    if secim == '3':
        print (num1-num2)
    if secim == '4':
        print (num1/num2)
    input()
