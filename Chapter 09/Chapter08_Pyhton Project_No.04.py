import random

def shuffleString(x, n):
	y = []
	b = 0

	while True:
		pola = ''.join(random.sample(x,len(x)))
		if pola not in y:
			y = y + [pola]
			b = b+1

		else:
			b = b

		if b == n:
			break
	print(y)

shuffleString("aku", 2)
shuffleString("aku", 3)
shuffleString("aku", 4)
shuffleString("12", 2)
