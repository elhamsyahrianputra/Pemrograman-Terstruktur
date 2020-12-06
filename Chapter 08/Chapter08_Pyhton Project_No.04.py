sayur = ["bayam", "kangkung", "wortel", "selada"]

while True:
	print("Menu:")
	print("A. Tambah data sayur")
	print("B. Hapus data sayur")
	print("C. Tampilkan data sayur")
	print("D. Keluar dari program")

	x = input("Pilihan anda:... ")
	print("")

	if x == "A" or x ==  "a":
		print("------------------------------------------")
		print("Anda ingin menambahkan data sayur")
		print("------------------------------------------")
		sayur.append(input("Silahkan masukkan nama sayur: "))
		print("")

	elif x == "B" or x == "b":
		try:
			print("------------------------------------------")
			print("Anda ingin menghapus data sayur")
			print("------------------------------------------")
			sayur.remove(input("Silahkan masukkan nama sayur: "))
			print("")
		except ValueError:
			print("Data tidak ditemukan")
			print("")

	elif x == "C" or x == "c":
		print("------------------------------------------")
		print("Ini adalah tampilan data sayur terkini")
		print("------------------------------------------")
		for nama in sayur:
			print(nama)
		print("")

	elif x == "D" or x == "d":
		print("TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI :-)")
		break

	else:
		print("Pilihan anda salah")
		print("")