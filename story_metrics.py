import os
import re
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from collections import Counter
from itertools import chain
from textrank import extract_key_phrases

def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text


def originality_score():
    # Load the story text files into a dictionary
    stories = defaultdict(str)
    for filename in os.listdir("stories"):
        if filename.endswith(".txt"):
            with open(os.path.join("stories", filename), "r") as f:
                stories[filename] = f.read()

    preprocessed_stories = {filename: preprocess_text(
        text) for filename, text in stories.items()}

    # Create a TF-IDF matrix
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_stories.values())

    # Compute the cosine similarity between each pair of stories
    cosine_similarities = cosine_similarity(tfidf_matrix)

    # Calculate the average cosine similarity score for each story
    avg_similarity_scores = {filename: cosine_similarities[i].mean(
    ) for i, filename in enumerate(stories.keys())}

    # Rank the stories by their average cosine similarity score
    ranked_stories = sorted(avg_similarity_scores.items(),
                            key=lambda x: x[1], reverse=True)

    # Print the ranked stories
    for filename, score in ranked_stories:
        print(f"Originality score for {filename}: {score}")


def diversity_score(story):
    words = TextBlob(story).words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    unique_words = set([word.lower()
                       for word in words if word.lower() not in stop_words])
    diversity = len(unique_words) / len(words)
    return diversity

def creativity_score(story):
    keywords = extract_key_phrases(story)
    rare_words = [word for word, count in Counter(chain.from_iterable(keywords)).items() if count == 1]
    creativity = len(rare_words) / len(keywords)
    return creativity

if __name__ == "__main__":

    originality_score()
    stories = []
    for i in range(0, 10):
        with open(f'stories/story_{i}.txt', 'r') as f:
            story = f.read()
            stories.append(story)

    for i, story in enumerate(stories):
        score = diversity_score(story)
        print(f"Diversity score for story {i}: {score}")

    for i, story in enumerate(stories):
        score = creativity_score(story)
        print(f"Creativity score for story {i}: {score}")
