import random

# jumlah score pemail mula-mula
score = 100

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
    score -= 2

# jika tebakan user lebih kecil dari angka
  elif (tebakan < angka):
    print("hehehe... Bilangan tebakan anda terlalu kecil")
    score -= 2

# jika tebakan user sama dengan angka
  else:
    print("yee... Bilangan tebakan anda BENAR :-)")
    break

# jumlah scroe user
if (score >= 0):
  print("Score Anda :",score)
else:
  print("Score Anda: 0")