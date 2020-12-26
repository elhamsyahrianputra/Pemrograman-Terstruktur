openfile = open("no2_input.txt", "r")

dataMhs = []
for i in openfile:
	data = i.split("|")
	dataMhs += [data]

listMhs = []
for data in dataMhs:
	dictMhs = dict({"nim":data[0], "nama":data[1], "alamat":data[2]})
	listMhs += [dictMhs]

inputnim = str(input("Masukkan NIM yang mau dicari : "))
print("")



end = 0
for i in listMhs:
	if inputnim in i.values():
		print("Data Mahasiswa")
		print("NIM\t\t:",i["nim"])
		print("Nama\t:",i["nama"])
		print("Alamat\t:",i["alamat"])
		end += 1
if end == 0:
	print("Data Mahasiswa tidak ditemukan")


openfile.close()	