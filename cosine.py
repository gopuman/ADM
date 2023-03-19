import os
import re
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the story text files into a dictionary
stories = defaultdict(str)
for filename in os.listdir("stories"):
    if filename.endswith(".txt"):
        with open(os.path.join("stories", filename), "r") as f:
            stories[filename] = f.read()

# Preprocess the text by removing stop words, punctuations, and converting to lowercase
def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text

preprocessed_stories = {filename: preprocess_text(text) for filename, text in stories.items()}

# Create a TF-IDF matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_stories.values())

# Compute the cosine similarity between each pair of stories
cosine_similarities = cosine_similarity(tfidf_matrix)

# Calculate the average cosine similarity score for each story
avg_similarity_scores = {filename: cosine_similarities[i].mean() for i, filename in enumerate(stories.keys())}

# Rank the stories by their average cosine similarity score
ranked_stories = sorted(avg_similarity_scores.items(), key=lambda x: x[1], reverse=True)

# Print the ranked stories
for filename, score in ranked_stories:
    print(f"{filename}: {score}")
