nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
		 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
		 {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
		 {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
		 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("====================================================================================")

print("NIM".ljust(15), end=""), print("NAMA".ljust(15), end="")
print("N.MID".ljust(15), end=""), print("N.UAS".ljust(15), end="")
print("N.AKHIR".ljust(15), end=""), print("STATUS")
print("------------------------------------------------------------------------------------")

for data in nilai:
	print(data["nim"].ljust(15), end="")
	print(data["nama"].upper().ljust(15), end="")
	print(str(data["mid"]).ljust(15), end="")
	print(str(data["uas"]).ljust(15), end="")

# N.AKHIR = (Nilai MID + 2*Nilai UAS)/3	
	nAkhir = (data["mid"]+(2*data["uas"]))//3
	print(str(nAkhir).ljust(15), end="")

	if nAkhir >= 60:
		print("LULUS")
	else:
		print("TIDAK LULUS")

print("------------------------------------------------------------------------------------")