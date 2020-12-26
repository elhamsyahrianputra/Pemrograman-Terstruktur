openfile = open("no1_input.txt", "r")
teks = openfile.read()
print(teks)
openfile.close()

print("")


openfile = open("no1_input.txt", "r")

ganjil = 0
genap = 0
for data in openfile:
	if ((int(data) % 2) == 0):
		genap += 1
	else:
		ganjil += 1

print("Banyaknya bilangan genap :",genap)
print("Banyaknya bialngan ganjil :", ganjil)
openfile.close()


