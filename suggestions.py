def resume_suggestions(ats, similarity, missing_skills):
    tips = []

    if ats < 70:
        tips.append("Improve resume formatting for ATS compatibility.")

    if similarity < 60:
        tips.append("Customize resume according to job description.")

    if missing_skills:
        tips.append("Add missing technical skills with projects.")

    if not tips:
        tips.append("Excellent resume alignment. Focus on interview prep.")

    return tips
