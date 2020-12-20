def bintang(n):
	if n%2 == 0:
		print("Input yang dimasukkan harus berupa huruf ganjil")

	else:
		n = (n+1) // 2
		for i in range(1, n):
			pola1 = ((i*2)-1) * "*"
			print(pola1.center(20))

		for i in range(n, 0, -1):
			pola2 = ((i*2)-1) * "*"
			print(pola2.center(20))
	print("")

bintang(7)
bintang(5)
bintang(4)



