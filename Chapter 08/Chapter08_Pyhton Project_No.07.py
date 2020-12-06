def hargaTermahal(listBuah):
	x = []
	for buah, harga in listBuah.items():
		dataBuah = (harga, buah)
		x.append(dataBuah)
	
	x.sort(reverse=True)
	namaBuah = list(x[0])
	print(namaBuah[1])

listBuah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7500, "duku" : 6500}
hargaTermahal(listBuah)