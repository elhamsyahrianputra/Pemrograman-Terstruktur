# Menampilkan isi dari file
myfile = open("no7_input.txt", "r")
readmyfile = myfile.read()
print(readmyfile)
myfile.close()

# Function untuk mengembalikan Sandi Caesar
def sCaesar(kalimat ,n):

    huruf = []
    for x in kalimat:
        ordHuruf = ord(x)
        huruf += [ordHuruf]
       
    hurufBaru = []
    for y in huruf:
        ordBaru = y - int(n)
        hurufBaru += [ordBaru]
       
    for z in hurufBaru:
        if z == 32 - int(n):
            ubahHuruf = chr(32)
            writeFile.write(str(ubahHuruf))
        elif z < 65:
            ubahHuruf = chr(z+26)
            writeFile.write(str(ubahHuruf))
        else:
            ubahHuruf = chr(z)
            writeFile.write(str(ubahHuruf))

# Memecah isi dari file menjadi beberapa sub String
openfile = open("no7_input.txt", "r")
splitData = []
for o in openfile:
    data = o.split("|")
    splitData += [data]

openfile.close()

print("")
print("")

# Menuliskan pengembalian Sandi Caesar ke dalam file baru
writeFile = open("no7_output.txt", "w")
for data in splitData:
    kalimat = data[0]
    n = data[1]
    sCaesar(kalimat,n)
    writeFile.write("\n")

writeFile.close()