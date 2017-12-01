from sklearn import preprocessing

def normalize(data):
	#data is an array
	normalizer = preprocessing.Normalizer().fit(data)
	return normalizer.transform(data)

#test normalize
X = [[ 1., -1.,  3.],
     [ 2.,  0.,  0.],
     [ 0.,  1., -1.]]

print(normalize(X))