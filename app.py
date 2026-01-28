import streamlit as st
import PyPDF2
import re

# -------------------------------
# FUNCTION: Extract text from PDF
# -------------------------------
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted
    return text


# -------------------------------
# FUNCTION: Extract skills
# -------------------------------
def extract_skills(text):
    skills_list = [
        "Python", "Java", "C", "C++", "SQL", "HTML", "CSS", "JavaScript",
        "Machine Learning", "Data Science", "React", "Node", "Django",
        "Flask", "AWS", "Excel", "Power BI"
    ]

    found_skills = []
    for skill in skills_list:
        if re.search(r"\b" + skill + r"\b", text, re.IGNORECASE):
            found_skills.append(skill)

    return list(set(found_skills))


# -------------------------------
# FUNCTION: Recommend Job Role
# -------------------------------
def recommend_job_role(skills):
    skills = [skill.lower() for skill in skills]

    if "python" in skills and "machine learning" in skills:
        return "Data Scientist"
    elif "java" in skills and "sql" in skills:
        return "Backend Developer"
    elif "html" in skills and "css" in skills and "javascript" in skills:
        return "Frontend Developer"
    else:
        return "Software Engineer"


# -------------------------------
# STREAMLIT UI
# -------------------------------
st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("Resume Analyzer Project")
st.write("Upload your resume (PDF) to analyze skills and get a job recommendation.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

# -------------------------------
# PROCESSING
# -------------------------------
if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    skills = extract_skills(resume_text)

    st.subheader("Extracted Resume Text")
    st.text(resume_text)

    if skills:
        st.subheader("Extracted Skills")
        st.write(", ".join(skills))

        job_role = recommend_job_role(skills)
        st.subheader("Recommended Job Role")
        st.success(job_role)
    else:
        st.warning("No skills found in the resume.")
