def calculate_score(resume_text):

    skills = [
        "python",
        "sql",
        "mysql",
        "flask",
        "opencv",
        "git",
        "machine learning"
    ]

    found_skills = []

    resume_text = resume_text.lower()

    for skill in skills:

        if skill in resume_text:
            found_skills.append(skill)

    score = round((len(found_skills) / len(skills)) * 100, 2)

    return score, found_skills