def ats_score(resume_text):
    score = 100

    word_count = len(resume_text.split())

    if word_count < 300:
        score -= 15
    if "@" not in resume_text:
        score -= 10
    if resume_text.count("\n") < 10:
        score -= 10
    if "experience" not in resume_text:
        score -= 10
    if "project" not in resume_text:
        score -= 10

    return max(score, 0)
