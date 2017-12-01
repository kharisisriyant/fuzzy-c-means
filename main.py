import csv
from utils import *
import pickle
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

def main():
	# ################################################################
	# ##################### FUZZY C-MEANS ############################
	# ################################################################

	# numericdata = []
	# centers = []

	# # Buka file data CencucIncome
	# file = open('data/CencusIncomeNumeric.data.txt', 'r')
	# reader = csv.reader(file)

	# # Masukin train data
	# for row in reader:
	# 	for i in range(len(row)):
	# 		row[i] = float(row[i])
	# 	numericdata.append(row)

	# # Initialize variable
	# n_attr = len(numericdata[0])
	# n_cluster = 2
	# m = 2
	# epsilon = 0.00001
	# isBreak = False
	# epoch = 1

	# # Initialize matrix U
	# matU = initialize(len(numericdata), n_cluster)

	# # Initialize centroid matrix
	# for i in range(n_cluster):
	# 	centers.append([0]*n_attr)

	# while not isBreak:
	# 	print(epoch)

	# 	# Fuzzy C Means
	# 	calculateCenterVector(matU, m, centers, numericdata)
	# 	isBreak = update_u(matU, numericdata, centers, m, epsilon)

	# 	epoch = epoch + 1

	# # Save Matrix U to file
	# with open('data/MatUFinal.data.pkl', 'wb') as f:
	# 	pickle.dump(matU, f)

	# ################################################################
	# ################## FUZZY C-MEANS DONE ##########################
	# ################################################################

	# GET Y TRAIN
	y_train = []

	# Buka file data CencucIncome
	file = open('data/CencusIncome.data.txt', 'r')
	reader = csv.reader(file)

	# Masukin train data
	for row in reader:
		temp_str = row[-1].strip()
		if(temp_str =="<=50K"):
			y_train.append(1)
		elif(temp_str==">50K"):
			y_train.append(0)

	# GET Y PREDICT	
	# Load Matrix U from file
	with open('data/MatUFinal.data.pkl', 'rb') as f:
		matU = pickle.load(f)

	y_predict = []

	for element in matU:
		if(element[0]>element[1]):
			y_predict.append(0)
		else:
			y_predict.append(1)

	print(f1_score(y_train, y_predict))
	print(accuracy_score(y_train, y_predict))

	
if __name__ == "__main__":
	main() ## with if