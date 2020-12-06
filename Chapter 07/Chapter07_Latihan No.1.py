print("Masukkan nama file:" ,end="  ")
namefile = str(input())

try:
	readfile = open(namefile, "r")
	print("Isi file", namefile, "adalah:")
	print("")
	print(readfile.read())

except FileNotFoundError:
	print("Maaf, file yang anda cari tidak ditemukan")
