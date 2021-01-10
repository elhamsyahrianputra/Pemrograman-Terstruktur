from datetime import *

myfile = open("no2_output.txt", "a")

while True:
	kodeMember = str(input("Masukkan Kode Member : "))
	namaMember = str(input("Masukkan Nama Member : "))
	judulBuku = str(input("Masukkan Judul Buku : "))

	dateNow = datetime.date(datetime.now())
	dateExp = dateNow + timedelta(days=7)

	myfile.write(kodeMember+"|"+namaMember+"|"+judulBuku+"|"+str(dateNow)+"|"+str(dateExp)+"\n")
	print("")

	pilihan = input("Ulangi lagi (y/n)?")
	if pilihan == "n":
		myfile.close()
		break

	print("")


