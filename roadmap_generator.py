def generate_roadmap(missing_skills):
    roadmap = {}

    for skill in missing_skills:
        roadmap[skill] = {
            "Learn": f"Online course or documentation for {skill}",
            "Practice": f"Mini project using {skill}",
            "Apply": f"Internship or certification in {skill}"
        }

    return roadmap
