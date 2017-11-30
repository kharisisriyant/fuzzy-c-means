import random
def initialize(numIns, numCls):
	#Inisialisasi matriks Uij
	#untuk setiap xi, total nilai xi pada j=0 s.d. j=N adalah 1

	matU = []
	for  i in range(numIns):
		totalProb = 0 #nilai batas bawah
		x = []
		upBorder=1
		for j in range(numCls):
			if (j != numCls-1):
				#random nilai val antara sum nilai xij dengan 1
				val = random.uniform(0,upBorder)
				totalProb = totalProb+val
				upBorder = 1-totalProb
			else:
				val = 1-totalProb
			x.append(val)
		matU.append(x)
	return matU

matU = initialize(5, 4)
print(matU)
