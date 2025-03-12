def min_max_finder():
    numbers = []  # Boş bir liste oluştur
    for i in range(5):  # Kullanıcıdan 5 adet sayı al
        num = int(input(f"{i+1}. sayıyı girin: "))
        numbers.append(num)

    min_number = min(numbers)  # En küçük sayıyı bul
    max_number = max(numbers)  # En büyük sayıyı bul

    print(f"Girilen sayılar: {numbers}")
    print(f"En küçük sayı: {min_number}")
    print(f"En büyük sayı: {max_number}")

# Fonksiyonu çağır
min_max_finder()