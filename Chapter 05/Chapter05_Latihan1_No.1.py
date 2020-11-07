# Input Nilai Ujian
bahasa = int(input("Masukkan Nilai Bahasa Indonesia :  "))
ipa = int(input("Masukkan Nilai Ipa 				:  "))
mtk = int(input("Masukkan Nilai Matematika 		:  "))


#Syrat Kelulusan
if (bahasa >= 0 and bahasa <= 100) and (ipa >= 0 and ipa <= 100) and (mtk >= 0 and mtk <= 100):

# jika nilai memenuhi syarat
	if (bahasa >= 60) and (ipa >= 60) and (mtk > 70):
		print("Status Kelulusan  				: LULUS")
# jika nilai tidak memneuhi syarat
	else:
		print("Status Kelulusan  				: TIDAK LULUS")

