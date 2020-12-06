# no.1 
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

# no.2
a.insert(3, 10)
b.insert(2, 16)

# no.3
a.append(4)
b.append(8)

# no.4
a.sort()
b.sort()

# no.5
import copy
c = copy.copy(a[0:7])
print(c)
d = copy.copy(b[2:9])
print(d)

# no.6
e = []
i = 0
for nilai in c:
	e = e + [nilai + d[i]]
	i = i + 1
print(e)

# no.7
e = tuple(e)
print(e)

# no.8
print(min(e))
print(max(e))
print(sum(e))

# no.9
f = "python adalah bahasa pemrograman yang menyenangkan"

# no.10
fSet = set(f)
print(fSet)

# no.11
fList = list(fSet)
fList.sort()
print(fList)