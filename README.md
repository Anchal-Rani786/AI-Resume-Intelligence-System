# AI Resume Intelligence System

An AI-powered resume screening system that analyzes resumes and compares them with job descriptions using NLP techniques.

## Features
- Resume PDF text extraction
- AI similarity score calculation
- Skill matching with job description
- Candidate-job compatibility analysis

## Technologies Used
- Python
- Natural Language Processing (NLP)
- Scikit-learn
- PyPDF

## How It Works
1. Resume is uploaded in PDF format
2. Text is extracted from the resume
3. Job description is provided as input
4. Cosine similarity compares both texts
5. System generates a match score

## Example Output

AI Resume Match Score: 25.36 %
Detected Skills: ['python', 'ml']
Missing Skills: ['sql', 'deep learning', 'data science']
Recommendation: Low match. Candidate should improve required skills.

## Future Improvements
- Web interface
- Resume ranking system
- AI-based resume improvement suggestions

## How to run
1. Install dependencies
pip install -r requirements.txt

2. Run the project
python main.py