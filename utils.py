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
				temp = pow(numerator/denominator, power_num)
				sum_result += temp

			# Instance = centroid
			if(sum_result==0):
				new_Uij = 1
			else:	
				new_Uij = 1/ sum_result

			diff_Uij = abs(u[i][j] - new_Uij)
			if(diff_Uij>epsilon):
				is_stop_iter = False
			u[i][j] = new_Uij
			
	return is_stop_iter