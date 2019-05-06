from .models import Movie, Review, Like, Dislike

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# dfReviews = pd.DataFrame(list(Review.objects.values_list('movie_id', 'rating', 'user_name_id')))


def recommending():
	dfLikes = pd.DataFrame(list(Like.objects.values_list('movie', 'user')))
	indices = pd.Series(dfLikes.index) #[0]index
	results = cosine_similarity(dfLikes, dfLikes)

	similar_movies = []

	idx = (indices.size)-1 #indices[indices == title_id].index[0] #(((indices.size)-1))
	score_series = pd.Series(results[idx]).sort_values(ascending=False)
	top_10_indexes = list(score_series.iloc[1:11].index)
	for i in top_10_indexes:
		similar_movies.append(list(dfLikes.index)[i])
	return similar_movies


