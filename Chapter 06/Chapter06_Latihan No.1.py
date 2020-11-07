# soal Chapter 06 Latihan No. 1

# Membuat fungsi rumus pyhtagoras
def isPythagoras(a, b, c):
	hasil = a**2 + b**2 == c**2
	print("a=",a,",b=",b,",c=",c," ->",hasil)

#  a. a=3, b=4, c=5  -> True
a = 3
b = 4
c = 5
isPythagoras(a, b, c)

#  b. a=5, b=9, c=12  -> False
a = 5
b = 9
c = 12
isPythagoras(a, b, c)

#  c. a=8, b=6, c=10  -> True
a = 8
b = 6
c = 10
isPythagoras(a, b, c)

#  d. a=7, b=8, c=11  -> False
a = 7
b = 8
c = 11
isPythagoras(a, b, c)