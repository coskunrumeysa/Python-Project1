# Öncelikle bu kod bloğunda bu kodu  yazan programcıyı tanıtıyoruz.
__author__ = "Rümeysa Coskun"

# İkinci olarak bu kod bloğuda  ilk kod olan "Merhaba Dünya Yazını ekrana basıyoruz."
print("Hello World")

# Üçüncü olarak bu kod bloğunda  girilen sayıya göre ilgili mesajların ekrana basılmasını sağlıyoruz.

print("Lutfen bir sayi seciniz")

print("Sabah ---1")
print("Oglen ---2")
print("Aksam ---3")
print("Gece  ---4")

choice = input("Lutfen seciminizi giriniz:")
isim = input("Lutfen isminizi giriniz :")

# print(type(isim))

# print(secim)

# print (isim)

if choice == "1":
    print("Hayirli Sabahlar", isim)

elif choice == "2":
    print("Hayirli Oglenler ", isim)

elif choice == "3":
    print("Hayirli  Aksamlar ", isim)

elif choice == "4":
    print("Hayirli Geceler", isim)

else:
    print("Gecersiz secim.")

# bazı operatörlerin kullanımı ve çıktısı
6+2
print(6+2)

6-2
print(6-2)

6*2
print(6*2)

6/2
print(6/2)

#karakterin çarpma işlemi ile beraber sayı ile kullaılması

"r"*10

print("r"*10)

"11" + "12"
print ("11" + "12")






