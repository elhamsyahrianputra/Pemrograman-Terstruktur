from datetime import *

listDate = []

def diffDate(x):

	listTgl = x.split("-")
	tgl1 = date.today()
	tgl2 = date(year = int(listTgl[0]), month = int(listTgl[1]), day = int(listTgl[2]))
	selisih = tgl2 - tgl1
	return selisih.days


print(diffDate("2021-03-14"))

