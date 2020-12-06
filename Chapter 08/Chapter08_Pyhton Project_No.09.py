listBuah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}

buah = input("Nama buah yang dibeli : ")
kg = int(input("Berapa kg				: "))
print("---------------------------------------")

total = listBuah[buah] * kg
print("Total harga				:", total)