from random import randint
jumlah = 0
while True:
	bil = randint(0, 10)
	jumlah += 1
	print(bil)
	if bil == 5:
		print("Jumlah perulangan : ",jumlah)
		break