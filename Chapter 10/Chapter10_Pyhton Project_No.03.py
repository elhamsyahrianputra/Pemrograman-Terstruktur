openfile = open("no2_input.txt", "r")
teks = openfile.read()
print(teks)
openfile.close()

openfile = open("no2_input.txt", "r")
dataMhs = []
for i in openfile:
	data = i.split("|")
	dataMhs += [data]

listMhs = []
for data in dataMhs:
	dictMhs = dict({"nim":data[0], "nama":data[1], "alamat":data[2]})
	listMhs += [dictMhs]
print(listMhs)

openfile.close()