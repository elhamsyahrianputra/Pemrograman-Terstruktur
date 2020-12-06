n = int(input("Berapa banyak yang ingin anda input: "))

dataBil = []
i = 1
for bil in range(n):
	x = int(input("Bilangan ke-" + str(i) + " :"))
	dataBil = dataBil + [x]
	i = i + 1
print(bil)
dataBil.sort(reverse=True)
print(dataBil)