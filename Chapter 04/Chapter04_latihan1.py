print("Tarif sewa untuk 12 jam pertama adalah Rp.200.000")
print("Jika waktu sewa lebih dari 12 jam, maka harga sewa setelah 12 jam akan bertambah Rp.10.000 perjamnya")
print("Waktu sewa dimulai dari pukul 06.00 sampai 23.50")
print("Maka waktu sewa customer tersebut ialah selama 17 jam 50 menit, lalu jika dibulatkan akan menjadi 18 jam")

#Jika x adalah waktu sewa
sewa = 18

print("Total tarif sewa rental mobil adalah Rp.",200000+((sewa-12)*10000))