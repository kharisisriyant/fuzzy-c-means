import csv

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

	reader.close()
	writer.close()

	file = open('data/CencusIncomeNumeric.data.txt', 'r')
	fw = open('data/CencusIncomeNumericNormalized.data.txt', 'w')
	reader = csv.reader(file)
	numericdata = []
	for row in reader:
		numericdata.append(row)

	numericdata = normalize(numericdata)

	writer = csv.writer(fw)
	for row in numericdata:
		writer.writerow(row)

	reader.close()
	writer.close()

if __name__ == "__main__":
	main() ## with if