# function untuk mencari jumlah data
def sum(*Mydata):
	jumlah = 0
	for bil in Mydata :
		jumlah += bil
	return jumlah

# function untuk mencara rata-rata data
def average(*Mydata):
# gunakan function len() untuk mencari banyak data dari Mydata
	rata_rata = sum(*Mydata)/len(Mydata)
	return rata_rata

# function untuk mencari nilai tertinggi data
def maks(*Mydata):
	max = 0
	for bil in Mydata :
		if bil > max :
			max = bil
		else:
			max = max
	return max

# function untuk mencari nilai terendah data
def min(*Mydata):
	minim = 99999
	for bil in Mydata :
		if bil < minim :
			minim = bil
		else:
			minim = minim
	return minim

