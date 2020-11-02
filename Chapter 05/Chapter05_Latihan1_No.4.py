# Memasukkan kode karyawan, nama karyawan, dan golongan
kode = input("Masukkan kode karyawan  :  ")
nama = input("Masukkan nama karyawan  :  ")
gol =  input("Masukkan golongan  :  ")

# pembagian gaji pokok dan potongan berdasarkan golongan
if (gol == "A") :
	pokok = 10000000
	potongan = 2.5
elif (gol == "B"):
	pokok = 8500000
	potongan = 2.0
elif (gol == "C"):
	pokok = 7000000
	potongan = 1.5
elif (gol == "D"):
	pokok = 5500000
	potongan = 1.0

# bagan struk gaji karyawan
print("=================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------------")

# output Nama karyawan
print("Nama Karyawan :",nama,"( Kode:",kode,")")

# output golongan
print("Golongan :",gol,)

print("---------------------------------")

# Output Gaji pokok
print("Gaji Pokok : Rp.",pokok)

#output potongan setelah di operasikan
hasil_potongan = pokok*(potongan/100)
print("Potongan (",potongan,"% ) : Rp.",hasil_potongan)

print("--------------------------------- -")

#Output perhitungan gaji bersih
print("Gaji Bersih : Rp.",pokok-hasil_potongan)