# Input Nilai Ujian
bahasa = int(input("Masukkan Nilai Bahasa Indonesia :  "))
ipa = int(input("Masukkan Nilai ipa 				:  "))
mtk = int(input("Masukkan Nilai Matematika		:  "))


#Syrat Kelulusan
if (bahasa >= 0 and bahasa <= 100) and (ipa >= 0 and ipa <= 100) and (mtk >= 0 and mtk <= 100):

	if (bahasa >= 60) and (ipa >= 60) and (mtk > 70):
		print("Status Kelulusan  				: LULUS")

	else:
		print("Status Kelulusan  				: TIDAK LULUS")
		print("Sebab     						: ")

		if (bahasa < 60):
			print("-  Nilai Bahasa Indonesia kurang dari 60")

		if (ipa < 60):
			print("-  Nilai IPA kurang dari 60")

		if (mtk <= 70):
			print("-  Nilai Matematika kurang dari 70")

else:
	print("Maaf input ada yang tidak valid")