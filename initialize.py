import random
def initialize(numIns, numCls):
	#Inisialisasi matriks Uij
	#untuk setiap ui, total nilai ui pada j=0 s.d. j=N adalah 1

	#matU:
	# 		| class 1 | class 2 | ... | class j
	# u1	|	val11 |  val12  | ... |  val1j
	# u2	|   val21 |  val22  | ... |  val2j
	# ...	|   ...   |   ...   | ... |  ...
	# ui 	|   vali1 |  val12  | ... |  valij

	matU = []
	for  i in range(numIns):
		totalProb = 0 #nilai batas bawah
		u = []
		upBorder=1
		for j in range(numCls):
			if (j != numCls-1):
				#random nilai val antara sum nilai uij dengan 1
				val = random.uniform(0,upBorder)
				totalProb = totalProb+val
				upBorder = 1-totalProb
			else:
				val = 1-totalProb
			u.append(val)
		matU.append(u)
	return matU

matU = initialize(5, 4)
print(matU)
