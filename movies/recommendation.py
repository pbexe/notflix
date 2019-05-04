from .models import Movie, Review

import numpy as np
import pandas as pd
x = []
vectors = {}
y = []
ms = {}

def jaccard_sim(x, y):
	if len(x) == len(y):
	    inter = np.logical_and(x,y)
	    union = np.logical_or(x,y)
	    similarity = inter.sum()/ float(union.sum())
#	    print similarity
	    return similarity

def comp_distance(x, y,i,id):
	jacc_dist = jaccard_sim(x,y)
	#try:
	#	mean = abs(ms[i][0] - ms[id][0])
	#	size = abs(ms[i][1] - ms[id][1])
	#except KeyError:
	#	mean = 5
	#	size = 1
	return jacc_dist

def getKNN(id, K):
	distance = []
	print(vectors)
	for i in vectors:
		if i != id:
			dist = comp_distance(vectors[i], vectors[id],i,id)
			distance.append((i, dist))
	distance = sorted(distance, key=lambda x: x[1], reverse=True)
	neighbors = []
	for j in range(K):
		neighbors.append(distance[j][0])
	return neighbors


def recommend(id):
	df = pd.DataFrame(list(Movie.objects.values_list('genre','movie_title')))
	df2 = pd.DataFrame(list(Review.objects.values_list('movie','rating')))
	print(df)
	y = df2.values.tolist()
	for i in y:
		ms[i[0]] = i[1]
	x = df.values.tolist()
	for i in x:
		vectors[i[1]] = list(map(int,i[0].split('|')))
	K = 500
	neighbors = getKNN(id, K)
	real_neighbors = []
	for i in neighbors:
		real_neighbors.append((i, ms[i][0] + ms[i][1]))
	real_neighbors = list(sorted(real_neighbors, key=lambda x: x[1], reverse=True))
	real=[]
	for i in real_neighbors:
		real.append(i[0])
#	print real
	return real

