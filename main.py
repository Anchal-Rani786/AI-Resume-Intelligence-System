from resume_parser import extract_text_from_pdf
from skill_matcher import calculate_match
from skill_gap import find_missing_skills


resume_path = "resume.pdf"

job_description = """
Looking for Python developer with machine learning,
SQL, deep learning and data science skills
"""


resume_text = extract_text_from_pdf(resume_path)
skills_list = ["python", "machine learning", "sql", "deep learning", "data science"]

resume_skills = []

for skill in skills_list:
    if skill in resume_text.lower():
        resume_skills.append(skill)

score = calculate_match(resume_text, job_description)

resume_skills = ["python", "machine learning", "sql"]
job_skills = ["python","ml", "machine learning", "deep learning", "sql", "data science"]

missing = find_missing_skills(resume_skills, job_skills)

def recommendation(score):
    if score >= 70:
        return "Excellent match for the job."
    elif score >= 40:
        return "Moderate match. Improve some skills."
    else:
        return "Low match. Candidate should improve required skills."
    
result = recommendation(score)

print("AI Resume Match Score:", score,"%")
print("Detected skills:" , resume_skills)
print("Missing Skills:", missing)
print("recommendation:" ,result)