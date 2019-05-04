from .models import Movie, Review, Like, Dislike
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

dfReviews = pd.DataFrame(list(Review.objects.values_list('movie_id', 'rating', 'user_name_id')))
indices = pd.Series(dfReviews.index)

dfLikes = pd.DataFrame(list(Like.objects.values_list('movie', 'user')))
dfDislikes = pd.DataFrame(list(Dislike.objects.values_list('movie', 'user')))

def recommending(title_id):

	results = cosine_similarity(dfReviews, dfReviews)

	recommended_movies = []
	idx = indices[indices == title_id].index[0]
	#print(idx)
	score_series = pd.Series(results[idx]).sort_values(ascending=False)
	top_10_indexes = list(score_series.iloc[1:11].index)
	for i in top_10_indexes:
		recommended_movies.append(list(dfReviews.index)[i])

	return recommended_movies

