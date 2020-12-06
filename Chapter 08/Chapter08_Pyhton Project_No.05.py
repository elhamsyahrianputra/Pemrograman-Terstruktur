def kuadrat(*bil):
	hasil = []
	for data in bil:
		hasil = hasil + [data**2]
	print(hasil)
	
kuadrat(2, 5, 4, 3, 10, 6)
