print("Daftar nama buah beserta harganya")
listBuah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}

for buah, harga in listBuah.items():
	print(buah, ":", harga)
print("")

total = 0
while True:
	buah = input("Nama buah yang dibeli : ")
	kg = int(input("Berapa kg				: "))
	total += listBuah[buah] * kg

	print("")
	penutup = input("Beli buah yang lain(y/n)? ")
	print("")
	if penutup == "n":
		print("---------------------------------")
		print("Total harga				:", total)
		break

