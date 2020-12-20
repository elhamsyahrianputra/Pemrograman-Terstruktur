def ubahHuruf(teks, a, b):
	listHuruf = list(teks)

	huruf = []
	for x in listHuruf:
		if x == a:
			x = b
		huruf = huruf + [x]
	huruf = ''.join(huruf)
	print(huruf)

ubahHuruf("ELHAM SYAHRIAN PUTRA", "A", "_")
ubahHuruf("MATEMATIKA", "T", "S")