nama = []
i = 1
while True:
	print("Masukkan nama mahasiswa ke-" + str(i) + ": ", end="")
	x = str(input())
	stop = input("Mau menambah nama mahasiswa? (y/n)?: ")
	if stop == "n":
		nama = nama + [x]
		break
	else :
		i = i + 1
		nama = nama + [x]

nama.sort()

for data in nama:
	print(data, "(" + str(len(data)), "karakter)")