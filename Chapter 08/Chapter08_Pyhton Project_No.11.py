listBuah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}

while True:
	print("Menu:")
	print("A. Tambah data buah")
	print("B. Beli buah")
	print("")
	pilihan = input("Pilihan menu: ")

	if pilihan == "A" or pilihan == "a":
		print("-----------------------------")
		namaBuah = input("Masukkan nama buah: ")
		if namaBuah in listBuah.keys():
			print("Nama buah yang anda masukkan sudah ada dalam data")
			print("-----------------------------")

		elif namaBuah not in listBuah:

			hargaBuah = int(input("Masukkan harga satuan: "))
			listBuah[namaBuah] = hargaBuah
			for buah, harga in listBuah.items():
				print("-   " + buah + " (Harga Rp." + str(harga) + ")")
			print("-----------------------------")


	elif pilihan == "B" or pilihan == "b":
		print("-----------------------------")
		total = 0

		while True:
			buah = input("Nama buah yang dibeli : ")
			kg = int(input("Berapa kg				: "))
			total += listBuah[buah] * kg

			print("-----------------------------")
			penutup = input("Beli buah yang lain(y/n)? ")
			print("-----------------------------")
			if penutup == "n":
				print("Total harga				: Rp." + str(total))
				break
		print("-----------------------------")

	else:
		print("-----------------------------")
		print("Pilihan yang anda masukkan tidak valid")
		print("-----------------------------")