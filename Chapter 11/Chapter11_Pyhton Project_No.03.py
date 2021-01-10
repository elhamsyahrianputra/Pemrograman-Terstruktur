from datetime import *

openfile = open("no2_output.txt", "r")


def diffDate(x):

	listTgl = x.split("-")
	tgl1 = date(year = int(listTgl[0]), month = int(listTgl[1]), day = int(listTgl[2]))	
	tgl2 = date.today()
	selisih = tgl2 - tgl1
	return selisih.days

dateNow = datetime.date(datetime.now())

dataMhs = []
for i in openfile:
	data = i.split("|")
	dataMhs += [data]

inputkode = str(input("Masukkan kode buku yang mau dicari : "))
print("")

end = 0
for i in dataMhs:
	if inputkode in i:
		print("Data Peminjamanan Buku")
		print("Kode Member\t\t\t\t\t:", i[0])
		print("Nama Member\t\t\t\t\t:", i[1])
		print("Judul Buku\t\t\t\t\t:", i[2])
		print("Tanggal Mulai Peminjaman\t:", i[3])
		print("Tanggal Maks Peminjaman\t\t:", i[4])
		print("Tanggal Pengembalian\t\t:", dateNow)

		selisihTgl = diffDate(i[4])

		if selisihTgl < 0:
			selisihTgl = 0

		print("Terlambat\t\t\t\t\t:", selisihTgl ,"hari")
		print("Denda\t\t\t\t\t\t:", "Rp.", 2000*selisihTgl)
		
		end += 1
		print("")

if end == 0:
	print("Data Mahasiswa tidak ditemukan")


openfile.close()	