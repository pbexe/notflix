import math*
def recommendation(movies, matrixV, userI) 
	pairtuplearr = []
	for k in range(len(users)):
		sum1=0
		sum2=0
		sum3=0
		for j in range(len(movies)):
			sum1=sum1+matrixV[userI][j]*matrixV[k][j]
			sum2=sum2+matrixV[userI][j]**2
			sum3=sum3+matrixV[k][j]**2
		sum2=sum2**(1/2)
		cosine_similarity=sum1/(sum2*sum3)
		pairtuple = (cosine_similarity, k)
		matrixCos[userI][k]=pairtuple
	matrixCos[userI]=sorted(matrixCos[userI], key=lambda x: x[0])
	for k in range(3):
		while movies[users[matrixCos[userI][k][1]]]!=1 and movies[users[userI]]!=null:
			movies.next();
			display(movies[users[userI]]);