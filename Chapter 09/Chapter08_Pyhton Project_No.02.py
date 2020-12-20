def bintang(n):
	for i in range(1, n+1):
		pola = ((i*2)-1) * "*"
		print(pola.center(2*n))

bintang(4)
bintang(5)
bintang(7)

