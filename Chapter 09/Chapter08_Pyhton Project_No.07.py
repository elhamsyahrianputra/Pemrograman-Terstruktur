mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print("===============================================================")

print("NIM".ljust(10), end=""), print("NAMA MAHASISWA".ljust(25), end="")
print("TGL LAHIR".ljust(15), end=""), print("TEMPAT LAHIR".ljust(10))

print("---------------------------------------------------------------")

listmhs = []
for i in mhs:
	listmhs = listmhs + [i.split(":")]

for data in listmhs:
	print(data[0].ljust(10), end="")
	print(data[1].ljust(25), end="")
	for tgl in listmhs:
		tglSplit = (data[2].split("-"))
		tglFidata = [tglSplit[2]]+[tglSplit[1]]+[tglSplit[0]]
	print("/".join(tglFidata).ljust(15), end='')
	print(data[3].ljust(10))

print("---------------------------------------------------------------")