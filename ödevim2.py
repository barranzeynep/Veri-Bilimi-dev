# Kullanıcıdan bir sayı alıyorum
sayi = int(input("Bir sayı girin: "))

# Negatif sayı kontrolü
if sayi < 0:
    print("Negatif sayı girdiniz!")
# Çift veya tek kontrolü
elif sayi % 2 == 0:
    print("Girdiğiniz sayı çifttir.")
else:
    print("Girdiğiniz sayı tektir.")