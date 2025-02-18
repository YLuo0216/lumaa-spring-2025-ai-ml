"""
This file preprocesses the original data downloaded from kaggle
"""
import pandas as pd
import spacy

DATA_PATH = 'wiki_movie_plots_deduped.csv'

def preprocess(input, nlp):
    if not input:
        return ''
    doc = nlp(input.lower())
    tokens = []
    for token in doc:
        if token.is_alpha and not token.is_stop:
            tokens.append(token.lemma_)
    return ' '.join(tokens)

if __name__ == "__main__":
    # load data
    data = pd.read_csv(DATA_PATH)
    # only keep relevant columns (title, genre, plot) with values
    # since this is a large dataset, I am filtering out rows without genres (unknown)
    # to retain the most helpful rows
    filtered_data = data[['Title', 'Genre', 'Plot']]
    filtered_data = filtered_data[filtered_data['Genre'] != 'unknown']

    # randomly select 500 to keep dataset manageable
    filtered_500 = filtered_data.sample(500, random_state=17)

    # create a new keyword column that combines genre and plot
    filtered_500['Description'] = filtered_500['Genre'] + ' ' + filtered_500['Plot']

    # use spacy to tokenize and lemmatize
    nlp = spacy.load("en_core_web_sm")
    filtered_500['Keywords'] = filtered_500['Description'].apply(lambda input: preprocess(input, nlp))
    filtered_500.drop(columns=['Description'], inplace=True)

    # save the processed data
    filtered_500.to_csv('preprocessed_500.csv', index=False)