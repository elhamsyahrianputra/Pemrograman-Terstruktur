# program menghitung faktorial
def faktorial(n):
	kali = 1
	for i in range (1, n+1):
		kali *= i
	return kali

# a. Kombinasi (5 ,3)
n = 5
a = 3

# rumus kombinasi 
# C(n, a) = n! / (a! (n-a)!)
print("C(5,3) =",faktorial(n)/(faktorial(a)*(faktorial(n-a))))



# b. Permutasi(10, 7)
n = 10
a = 7

# rumus permutasi
# P(n ,a) = n! / (n-a)!
print("P(10,7) =",faktorial(n)/(faktorial(n-a)))