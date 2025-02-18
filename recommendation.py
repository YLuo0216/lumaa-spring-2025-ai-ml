"""
This file recommends movies based on user queries
"""

import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import preprocess

# load preprocessed data
DATA_PATH = 'preprocessed_500.csv'
data = pd.read_csv(DATA_PATH)

# use tf-idf to vectorize the movie keywords
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(data['Keywords'])

# preprocess user queries and perform similarity search for recommendations
# returns the top 5 movies by default and similarity scores
def recommend(user_query, n=5):
    nlp = spacy.load("en_core_web_sm")
    processed_query = preprocess(user_query, nlp)
    user_vector = vectorizer.transform([processed_query])
    similarity_scores = cosine_similarity(user_vector, tfidf)[0]
    top_n_index = similarity_scores.argsort()[-n:][::-1]
    return top_n_index, similarity_scores[top_n_index]

# prompt for user input and makes recommendation
if __name__ == "__main__":
    # takes user input
    user_query = input("What are your preferences? ")
    
    # output the recommendations
    print("Here are your top movie recommendations:\n")
    recommendation_index, scores = recommend(user_query)
    movies = data.iloc[recommendation_index].copy()
    movies['Scores'] = scores
    for _, row in movies.iterrows():
        movie_info = (
            f"Title: {row['Title']}\n"
            f"Genre: {row['Genre']}\n"
            f"Plot: {row['Plot']}\n"
            f"Similarity Score: {row['Scores']:.3f}\n"
        )
        print(movie_info)
