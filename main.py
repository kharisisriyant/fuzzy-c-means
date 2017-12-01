import csv
from initialize import initialize
from normalize import normalize
from utils import *

def calculateCenterVector(matU, m, centers, matX):
	for j, c_j in enumerate(centers):
		sigma_uijm_xi = []
		sigma_uijm = 0.0
		for i in range(len(matX)):
			sigma_uijm = sigma_uijm + pow(matU[i][j], 2/(m-1))

			if (i == 0):
				for a in range(len(c_j)):
					sigma_uijm_xi.append(pow(matU[i][j], 2/(m-1)) * matX[i][a])
			else:
				for a in range(len(c_j)):
					sigma_uijm_xi[a] = sigma_uijm_xi[a] + pow(matU[i][j], 2/(m-1)) * matX[i][a]

		#belum dites
		for a in range(len(c_j)):
			c_j[a] = sigma_uijm_xi[a] / sigma_uijm

def main():
	#buka file data CencucIncome
	file = open('data/CencusIncomeNumeric.data.txt', 'r')
	reader = csv.reader(file)
	numericdata = []
	centers = []

	for row in reader:
		for i in range(len(row)):
			row[i] = float(row[i])
		numericdata.append(row)

	n_attr = len(numericdata[0])
	n_cluster = 2
	m = 2
	epsilon = 0.01

	matU = initialize(len(numericdata), n_cluster)

	#inisialisasi centers
	for i in range(n_cluster):
		centers.append([0]*n_attr)

	isBreak = False
	i = 1
	while not isBreak:
		print(i)

		#update centers
		calculateCenterVector(matU, m, centers, numericdata)

		isBreak = update_u(matU, numericdata, centers, m, epsilon)
		print(isBreak)

		i = i + 1

	matU = initialize(len(numericdata), n_cluster)
	fw = open('data/MatUFinal.data.txt', 'w')
	print(matU, end="\n", file=fw)
	fw.close()

	# for i in matU:
	# 	for j in i:
	# 		print(str(j) + " - ")
	# 	print()
if __name__ == "__main__":
	main() ## with if