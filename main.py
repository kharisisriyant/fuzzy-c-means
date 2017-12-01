import csv

def calculateCenterVector():
	for j, c_j in enumerate(centers):
		sigma_uijm_xi = []
		sigma_uijm = 0
		for i, x_i in enumerate(x):
			sigma_uijm = sigma_uijm + pow(u[i][j], 2)

			if (i == 0):
				for a in range(len(c_j)):
					sigma_uijm_xi = sigma_uijm_xi + pow(u[i][j], 2) * x_i[a]
			else:
				for a, att in range(len(c_j)):
					sigma_uijm_xi[a] = sigma_uijm_xi[a] + pow(u[i][j], 2) * x_i[a]

		for a, att in enumerate(c_j):
			att = sigma_uijm_xi[a] / sigma_uijm

def calculateXMinC(x, c):
	res = []
	for i in range(len(x)):
		res.append(x[i]-c[i])

	#calculate magnitud res
	mag = 0
	for i in range(len(res)):
		mag = mag+pow(res[i], 2)

	return pow(mag,0.5)

def calculateSum(varToSum, N):
	res = 0
	for i in range(N):
		res = res+varToSum[i]
	return res

def update(matU, m, c):
	#update matriks U[k] menjadi U[k+1]
	#m is a float number greather than 1 (defined)
	#c is list center of vectors
	#assume name of matrix data: x

	for i in range(len(matU)):
		for j in range(len(matU[i])):
			sumDiv = 0
			xiMinCj = calculateXMinC(x[i]-c[j])
			for k in range(len(x[i])):
				xiMinCk = calculateXMinC(x[i]-c[k])
				#ximincj/ximinck
				divNoPow = xiMinCj/xiMinCk
				#pangkatkan
				divPow = pow(divNoPow, (2/m-1))
				#sum
				sumDiv = sumDiv+divPow
			u[i][j] = 1/sumDiv

def checkStop(matUnext,matUnow, epsilon):
	#calculate matU2-matU1
	uNextMinNow = []
	for i in range(len(matU2)):
		u = []
		for j in range(len(matU2)):
			u.append(matUnext[i][j]-matUnow[i][j])
		uNextMinNow.append(u)

	#calculate max uNextMinNowij
	max = uNexMinNow[0][0]
	for i in range(len(uNextMinNow)):
		for j in range(len(uNextMinNow[i])):
			if (max < uNextMinNow[i][j]):
				max = uNextMinNow[i][j]

	if (max < epsilon):
		return True
	else:
		return False

def main():
	#buka file data CencucIncome
	file = open('data/CencusIncomeNumericFix.data.txt', 'w')
	reader = csv.reader(file)
	writer = csv.writer(fw)
	numericdata = []
	for row in reader:
		datarow = [row[0], row[2], row[4], row[10], row[11], row[12]]
		writer.writerow(datarow)
		numericdata = numericdata + datarow

if __name__ == "__main__":
	main() ## with if
