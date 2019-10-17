

tabla = [[0 for x in range(5)] for y in range(2)]




for x in tabla:
	for y in x:
		print ":"+str(y)
	print "*"*10


tabla[1][2] = 345
print "fsdfs"

for x in tabla:
	for y in x:
		print (":"+str(y))
	print "*"*10