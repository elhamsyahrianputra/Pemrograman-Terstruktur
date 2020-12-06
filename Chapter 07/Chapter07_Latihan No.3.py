print("------------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("------------------------------")

bil = 0
n = 0
while True:
	try:
		bil = bil + int(input("Masukkan bilangan bulat: "))
		n = n + 1
	except ValueError:
		print("Bukan bilangan bulat")
		
	penutup = input("Lagi (y/n)? : ")
	if penutup == "n":
		rata_rata = bil/n
		print("Rata-ratanya adalah: ", rata_rata)
		break
