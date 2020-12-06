def averageBuah(listBuah):
	sum = 0
	for harga in listBuah.values():
		sum = sum + harga
	hasil = sum/len(listBuah)
	print(hasil)
	
listBuah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7500, "duku" : 6500}
averageBuah(listBuah)