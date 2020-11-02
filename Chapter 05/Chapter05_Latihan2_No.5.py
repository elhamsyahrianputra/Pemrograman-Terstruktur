import random

# perkenal game kepada user
print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!")

# menentukan angka yang ditebak oleh user
angka = random.randint(0, 100)

# perintah untukl menyruh user memasukkan angkta tebakan
while True:
  tebakan = int(input("Tebakan anda: "))

# jika tebakan user lebah besar dari angka
  if (tebakan > angka):
    print("hehehe... Bilangan tebakan anda terlalu besar")

# jika tebakan user lebih kecil dari angka
  elif (tebakan < angka):
    print("hehehe... Bilangan tebakan anda terlalu kecil")

# jika tebakan user sama dengan angka
  else:
    print("yee... Bilangan tebakan anda BENAR :-)")
    break