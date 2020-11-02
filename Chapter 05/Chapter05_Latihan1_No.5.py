# Memasukkan kode karyawan, nama karyawan, dan golongan
kode = input("Masukkan kode karyawan       		:  ")
nama = input("Masukkan nama karyawan       	        :  ")
gol =  input("Masukkan Golongan 		 	:  ")
nikah = int(input("Masukkan status(1:menikah, 2:belum) 	:  "))

if (nikah == 1):
        anak = int(input("Masukkan jumlah anak 	                :  "))
elif (nikah == 2):
	anak = int(0)

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
print("====================================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("----------------------------------------------------")

# output Nama karyawan
print("Nama Karyawan 			:",nama,"( Kode:",kode,")")

# output golongan
print("Golongan 			:",gol,)

# output menikah
if (nikah == 1):
	print("Status Menikah 			: Menikah")
elif (nikah == 2):
	print("Statis menikah 			: Belum menikah")

# output jumlah anak
if (nikah == 1):
	print("Jumlah Anak 			: ",anak)

print("----------------------------------------------------")

# Output Gaji pokok
print("Gaji Pokok 			: Rp.",pokok)

# menghitung tunjangan istri/suami
if (nikah == 1):
	tunjangan_istrisuami = pokok*(10/100)
	print("Tunjangan Istri/Suami 	        : Rp.",tunjangan_istrisuami)
elif (nikah == 2):
        tunjangan_istrisuami = 0
        print("Tunjangan Istri/Suami 	        : Rp.",tunjangan_istrisuami)
        
# menghitung tunjangan anak
tunjangan_anak = anak*(pokok*(5/100))
print("Tunjangan Anak 			: Rp.",tunjangan_anak)

print("---------------------------------------------------- +")

# menghitung gaji kotor
gaji_kotor = pokok+tunjangan_istrisuami+tunjangan_anak
print("Gaji Kotor                     : Rp.",gaji_kotor)

# menghitung total potongan
hasil_potongan = gaji_kotor*(potongan/100)
print("Potongan (",potongan,"% )               : Rp.",hasil_potongan)

print("---------------------------------------------------- -")
# menghitung gaji bersih
print("Gaji Bersih 			: Rp.",gaji_kotor-hasil_potongan)
