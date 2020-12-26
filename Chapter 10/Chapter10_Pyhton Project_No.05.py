openfile = open("no5_input.txt", "r")
teks = openfile.read()
print(teks)
openfile.close()


readfile = open("no5_input.txt", "r")

dataBil = []
for bil in readfile:
	data = bil.split("|")
	dataBil += [data]

print("")
print("")

readfile.close()

writefile = open("no5_output.txt", "w")
for sum in dataBil:
	hasilBil = int(sum[0]) + int(sum[1])
	writefile.write(str(hasilBil)+"\n")
writefile.close()