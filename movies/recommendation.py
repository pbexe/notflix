from .models import Movie, Review, Like, Dislike

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# dfReviews = pd.DataFrame(list(Review.objects.values_list('movie_id', 'rating', 'user_name_id')))


def recommending(title_id):
	dfLikes = pd.DataFrame(list(Like.objects.values_list('movie', 'user')))
	dfMovies = pd.DataFrame(list(Movie.objects.values_list('id', 'genre')))
	#last liked movie id
	# print("this is movie id  ", Like.objects.latest('id').movie.pk)
	# print(dfMovies)
	# print("here   ", dfLikes.get(0)[3])
	indices = pd.Series(dfMovies.index) #[0]index
	results = cosine_similarity(dfMovies, dfMovies)
	print(results)
	similar_movies = []

	idx = title_id #Like.objects.latest('id').movie.pk #indices[indices == title_id].index[0] #(indices.size)-1
	# print("this is idx  ", idx)
	score_series = pd.Series(results[idx]).sort_values(ascending=False)
	top_5_indexes = list(score_series.iloc[1:6].index)
	print (top_5_indexes)

	return top_5_indexes

	# # print (top_10_indexes)
	# for i in top_5_indexes:
	# 	similar_movies.append(list(dfMovies.index)[i])
	# print(similar_movies)
	# return similar_movies


