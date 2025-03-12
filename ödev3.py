# Kullanıcıdan bir sayı alıyorum.
sayi = int(input("Bir sayı girin: "))

# For döngüsü ile toplam hesaplama yapıyorum.
toplam_for = 0
for i in range(1, sayi + 1):
    toplam_for += i

# While döngüsü ile toplam hesaplama yapıyorum.
toplam_while = 0
i = 1
while i <= sayi:
    toplam_while += i
    i += 1

# Sonuçları ekrana yazdır
print(f"For döngüsü ile toplam: {toplam_for}")
print(f"While döngüsü ile toplam: {toplam_while}")
