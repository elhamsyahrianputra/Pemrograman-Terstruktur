nilaiMhs = [{"nim" : "A01", "nama" : "Amir", "mid" : 50, "uas" : 80}, 
			{"nim" : "A02", "nama" : "Budi", "mid" : 40, "uas" : 90}, 
			{"nim" : "A03", "nama" : "Cici", "mid" : 50, "uas" : 50}, 
			{"nim" : "A04", "nama" : "Dedi", "mid" : 20, "uas" : 30}, 
			{"nim" : "A05", "nama" : "Fifi", "mid" : 70, "uas" : 40}]


def nilaiTertinggi():
	mhs = []
	for nilai in nilaiMhs:
		nilaiAkhir =(nilai["mid"]+(2*nilai["uas"]))/3, nilai["nim"], nilai["nama"]
		mhs = mhs + [nilaiAkhir]
	mhs.sort(reverse=True)
	mhsAkhir = mhs[0]
	print(mhsAkhir[1], mhsAkhir[2])
print("Siswa beserta NIMnya yang mendapatkan nilai akhir paling tinggi adalah ")
nilaiTertinggi()

