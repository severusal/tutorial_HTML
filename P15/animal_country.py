f = open("country_animals.txt", "r")
line1 = f.readline()
line2 = f.readline()
data=[]
while line1:
	data.append([line1, line2])

	line1 = f.readline()
	line2 = f.readline()

print(data)