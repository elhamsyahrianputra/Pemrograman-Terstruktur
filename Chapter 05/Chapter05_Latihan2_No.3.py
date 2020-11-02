banyak = 0
jumlah = 0
for ganjil in range(100):
	if ganjil % 2 != 0:
		print(ganjil)
		banyak += 1
		jumlah = jumlah + ganjil
print("Banyaknya bilangan ganjil :",banyak)
print("Jumlah seluruh bilangan : ",jumlah)