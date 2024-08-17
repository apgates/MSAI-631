from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def retrieve(query, documents):
    vectorizer = TfidfVectorizer().fit_transform(documents + [query])
    vectors = vectorizer.toarray()
    cosine_similarities = cosine_similarity(vectors[-1], vectors[:-1])
    most_similar_doc_idx = np.argmax(cosine_similarities)
    return documents[most_similar_doc_idx]
