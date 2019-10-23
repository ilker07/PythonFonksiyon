


def bolme(sayi1,sayi2,bolunecek):
    toplam=0
    for i in range(sayi1,sayi2):
        if(i%bolunecek==0):
            toplam +=i


    return toplam


def kontrol(deger,sayi=0):
    if(deger<=0):
        raise Exception("Hata2")
    if(deger>=sayi and sayi!=0):
        raise Exception("Hata1")

while(1):
 try:
    sayi1 = int(input("İlk sayiyi giriniz:"))
    kontrol(sayi1)
    sayi2 = int(input("İkinci sayiyi giriniz:"))
    kontrol(sayi2)
    assert sayi2>sayi1  #2.sayi 1.den büyük olmalı.
    bolunecek = int(input("Bölünecek sayiyi giriniz:"))  #Bolunecek sayi 2 den küçük olmalı.
    kontrol(bolunecek,sayi2)


    break

 except ValueError:
    print("Rakam olmayan bir ifade girdiniz.")

 except AssertionError:
     print("İkinci girdiğiniz değer birinciden büyük olmalı!!")

 except Exception as e:
     if(e.args[0]=="Hata1"):
         print("Girdiğiniz ikinci sayi bölünecek sayıdan büyük olmalı.")
     else:
      print("0 dan küçük değer giremezsiniz!!")

print("Bölünen değerlerin toplamı:",bolme(sayi1,sayi2,bolunecek))




