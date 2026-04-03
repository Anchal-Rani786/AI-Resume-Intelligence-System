from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match(resume_text, job_description):

    text = [resume_text, job_description]

    cv = CountVectorizer()
    matrix = cv.fit_transform(text)

    similarity = cosine_similarity(matrix)

    score = similarity[0][1] * 100

    return round(score,2)