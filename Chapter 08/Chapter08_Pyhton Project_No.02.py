def dataStat(x):
	a = sum(x)/len(x)
	b = max(x)
	c = min(x)
	data = [a] + [b] + [c]
	return data

x = [5, 4, 8, 3, 1, 10, 15, 14, 7, 8]
print(dataStat(x))