print("Masukkan nama file: ", end=" ")
namefile = str(input())
file = open(namefile, "a")

while True:
	print("Data yang mau ditambahkan: ", end=" ")
	file.write(input())
	lagi = input("Mau lagi (y/n): ")
	if lagi == "n":
		file.close()
		break




