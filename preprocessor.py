import csv
from utils import normalize
from utils import normalizeTestData

def main():
	#buka file data CencucIncome, ambil semua data numeric
	file = open('data/CencusIncome.data.txt', 'r')
	fw = open('data/CencusIncomeNumeric.data.txt', 'w')
	reader = csv.reader(file)
	writer = csv.writer(fw)
	numericdata = []
	for row in reader:
		datarow = [row[0], row[2], row[4], row[10], row[11], row[12]]
		writer.writerow(datarow)
		numericdata = numericdata + datarow

	file.close()
	fw.close()

	file = open('data/CencusIncomeNumeric.data.txt', 'r')
	fw = open('data/CencusIncomeNumericNormalized.data.txt', 'w')
	reader = csv.reader(file)
	numericdata = []
	for row in reader:
		numericdata.append(row)

	preprocessTestData(numericdata)

	numericdata = normalize(numericdata)

	writer = csv.writer(fw)
	for row in numericdata:
		writer.writerow(row)

	file.close()
	fw.close()

def preprocessTestData(dataTrain):
	#buka file data CencucIncome, ambil semua data numeric
	file = open('data/CencusIncome.test.txt', 'r')
	fw = open('data/CencusIncomeNumeric.test.txt', 'w')
	reader = csv.reader(file)
	writer = csv.writer(fw)
	numericdata = []
	for row in reader:
		datarow = [row[0], row[2], row[4], row[10], row[11], row[12]]
		writer.writerow(datarow)
		numericdata = numericdata + datarow

	file.close()
	fw.close()

	file = open('data/CencusIncomeNumeric.test.txt', 'r')
	fw = open('data/CencusIncomeNumericNormalized.test.txt', 'w')
	reader = csv.reader(file)
	numericdata = []
	for row in reader:
		numericdata.append(row)

	numericdata = normalizeTestData(dataTrain, numericdata)

	writer = csv.writer(fw)
	for row in numericdata:
		writer.writerow(row)

	file.close()
	fw.close()

if __name__ == "__main__":
	main() ## with if