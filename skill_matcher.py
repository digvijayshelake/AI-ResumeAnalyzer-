def match_skills(found_skills, required_skills):
    matched = []
    missing = []

    for skill in required_skills:
        if skill in found_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = int((len(matched) / len(required_skills)) * 100)
    return matched, missing, score
