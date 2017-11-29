import csv

def main():
	#buka file data CencucIncome
	file = open('data/CencusIncome.data.txt', 'r')
	fw = open('data/CencusIncomeNumericFix.data.txt', 'w')
	reader = csv.reader(file)
	writer = csv.writer(fw)
	numericdata = []
	for row in reader:
		datarow = [row[0], row[2], row[4], row[10], row[11], row[12]]
		writer.writerow(datarow)
		numericdata = numericdata + datarow

if __name__ == "__main__":
	main() ## with if