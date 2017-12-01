import random
from sklearn import preprocessing

def normalize(data):
	#data is an array
	normalizer = preprocessing.Normalizer().fit(data)
	return normalizer.transform(data)

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

# Count the distance between instance and centroid of a cluster
# instance, centroid --> array of double
# PRECONDITION : size of instance = size of centroid
def count_distance(instance, centroid):
	q = 2 # Using euclidean
	sum_result = 0
	for i in range(0, len(instance)):
		temp = instance[i]-centroid[i]
		temp = pow(temp, q)
		sum_result += temp

	root = 1/q
	distance = pow(sum_result, root)
	return distance

def update_u(u, instances, centroids, m, epsilon):
	is_stop_iter 	= True
	n_row 			= len(instances)
	n_centroids 	= len(centroids)

	for i in range(0, n_row):
		for j in range(0, n_centroids):
			# initialize variable
			Xi 			= instances[i]
			Cj 			= centroids[j]
			power_num 	= 2/(m-1)
			sum_result 	= 0
			numerator 	= count_distance(Xi, Cj) 			# Pembilang

			# Hitung sigma
			for k in range(0, n_centroids):
				Ck 			= centroids[k]
				denominator = count_distance(Xi, Ck) 		# Penyebut
				temp 		= pow(numerator/denominator, power_num)
				sum_result 	+= temp

			# Instance == centroid
			if(sum_result==0):
				new_Uij = 1
			else:	
				new_Uij = 1/ sum_result

			diff_Uij = abs(u[i][j] - new_Uij)
			if(diff_Uij>epsilon):
				is_stop_iter = False
			u[i][j] = new_Uij
			
	return is_stop_iter