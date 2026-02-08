import streamlit as st

from resume_parser import extract_text_from_pdf
from job_roles import job_roles
from skill_database import SKILLS_DB
from skill_extractor import extract_skills
from similarity_engine import resume_job_similarity
from ats_checker import ats_score
from skill_matcher import match_skills
from roadmap_generator import generate_roadmap
from suggestions import resume_suggestions

st.set_page_config("AI Resume Analyzer VAST", layout="wide")

st.title("🚀 AI Resume Analyzer & Skill Gap Finder (VAST Version)")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

job_choice = st.selectbox("Select Job Role", list(job_roles.keys()))
custom_jd = st.text_area("Or Paste Custom Job Description (Optional)")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)

    job_text = custom_jd.lower() if custom_jd else " ".join(job_roles[job_choice])

    found_skills = extract_skills(resume_text, SKILLS_DB)

    matched, missing, skill_score = match_skills(
        found_skills, job_text.split()
    )

    similarity = resume_job_similarity(resume_text, job_text)
    ats = ats_score(resume_text)

    st.subheader("📊 Scores")
    col1, col2, col3 = st.columns(3)
    col1.metric("Skill Match %", skill_score)
    col2.metric("ATS Score", ats)
    col3.metric("JD Similarity %", similarity)

    st.subheader("✅ Matched Skills")
    st.success(", ".join(matched) if matched else "None")

    st.subheader("❌ Missing Skills")
    st.error(", ".join(missing) if missing else "None")

    st.subheader("🧠 Improvement Suggestions")
    for tip in resume_suggestions(ats, similarity, missing):
        st.write("•", tip)

    st.subheader("📚 Learning Roadmap")
    roadmap = generate_roadmap(missing)
    for skill, steps in roadmap.items():
        st.markdown(f"### {skill}")
        for k, v in steps.items():
            st.write(f"- **{k}:** {v}")
