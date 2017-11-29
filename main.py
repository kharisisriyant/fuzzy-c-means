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
