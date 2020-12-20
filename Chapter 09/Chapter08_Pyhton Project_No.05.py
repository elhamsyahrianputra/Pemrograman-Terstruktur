nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
		 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
		 {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
		 {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
		 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("===================================================================")
print("")

print("NIM".ljust(15), end=""), print("NAMA".ljust(15), end="")
print("N.MID".ljust(15), end=""), print("N.UAS".ljust(15))
print("-------------------------------------------------------------------")

for data in nilai:
	print(data["nim"].ljust(10), end="")
	print(data["nama"].upper().ljust(15), end="")
	print(str(data["mid"]).ljust(15), end="")
	print(data["uas"])

print("-------------------------------------------------------------------")

