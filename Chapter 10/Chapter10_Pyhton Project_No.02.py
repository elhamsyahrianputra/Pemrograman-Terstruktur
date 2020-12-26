openfile = open("no2_input.txt", "a")

while True:
	nim = str(input("Masukkan NIM\t\t: "))
	nama = str(input("Masukkan Nama Mhs\t: "))
	alamat = str(input("Masukkan Alamat\t\t: "))
	print("")

	openfile.write(nim+"|"+nama+"|"+alamat+"\n")

	ulang = str(input("Ulangi input lagi? (y/n)\t:"))
	print("")
	if ulang == "n" :
		openfile.close()
		break
