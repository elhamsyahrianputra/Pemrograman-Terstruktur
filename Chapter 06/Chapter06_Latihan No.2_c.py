def starFormation1(n):
	for star in range(1, n+1):
		print(star * "*")

def starFormation2(n):
	for star in range (1, n+1):
		print((n+1-star) * "*")

def starFormation3(n):
	starFormation1(n//2)
	starFormation2(n-(n//2))

starFormation3(7)