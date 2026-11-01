import streamlit as st
import re
import json
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Resume Skill Matcher",
    page_icon="📄",
    layout="wide"
)

class SkillAnalyzer:
    """Core logic class handling skill extraction and matching."""
    
    def __init__(self):
        # Database of domain skills
        self.skill_bank = {
            "programming": ["python", "c++", "java", "sql", "javascript", "html", "css"],
            "ai_ml": ["machine learning", "deep learning", "nlp", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch"],
            "core_cs": ["dsa", "dbms", "operating systems", "computer networks", "oop"]
        }

    def extract_skills(self, text):
        """Extracts known skills from input text using Regex word boundaries."""
        cleaned_text = text.lower()
        found_skills = set()
        
        all_known_skills = [skill for sublist in self.skill_bank.values() for skill in sublist]
        
        for skill in all_known_skills:
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, cleaned_text):
                found_skills.add(skill)
                
        return found_skills

    def calculate_match(self, resume_skills, job_skills):
        """Calculates set intersection and match percentage."""
        if not job_skills:
            return 0.0, set(), set()
            
        matched_skills = resume_skills.intersection(job_skills)
        missing_skills = job_skills.difference(resume_skills)
        
        match_score = (len(matched_skills) / len(job_skills)) * 100
        return round(match_score, 2), matched_skills, missing_skills


# Initialize Backend Logic
analyzer = SkillAnalyzer()

# --- STREAMLIT UI ---
st.title("📄 AI Resume & Job Skill Matcher")
st.caption("Interactive MCA Mini-Project | Topic: Text Parsing & Set Operations")

st.markdown("---")

# Input Section - 2 Columns
col1, col2 = st.columns(2)

default_resume = """
Targeting entry-level AI Engineer roles. Proficient in Python, SQL, and Data Structures (DSA).
Hands-on experience with Pandas, NumPy, Machine Learning algorithms, and Object-Oriented Programming (OOP).
"""

default_jd = """
Looking for an AI Trainee. Must have strong fundamentals in Python, C++, DSA, and DBMS.
Required skills include Machine Learning, NLP, Pandas, and PyTorch. OOP knowledge is mandatory.
"""

with col1:
    st.subheader("1. Resume Content")
    resume_input = st.text_area("Paste candidate resume here:", value=default_resume, height=220)

with col2:
    st.subheader("2. Job Requirement")
    jd_input = st.text_area("Paste job description here:", value=default_jd, height=220)

# Action Button
st.write("")
analyze_btn = st.button("🔍 Analyze Match Compatibility", type="primary", use_container_width=True)

# Output Section
if analyze_btn:
    if not resume_input.strip() or not jd_input.strip():
        st.error("Please provide text in both fields to proceed.")
    else:
        # Perform Analysis
        resume_skills = analyzer.extract_skills(resume_input)
        jd_skills = analyzer.extract_skills(jd_input)
        score, matched, missing = analyzer.calculate_match(resume_skills, jd_skills)

        st.markdown("---")
        st.header("📊 Matching Results")

        # Top Banner Metrics
        metric_col1, metric_col2 = st.columns([1, 2])
        
        with metric_col1:
            st.metric(label="Match Score", value=f"{score}%")
            
        with metric_col2:
            st.write("Overall Qualification Level:")
            st.progress(score / 100)

        # Skill Tag Breakdown
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            st.subheader("✅ Matched Skills")
            if matched:
                for item in matched:
                    st.success(f"• {item.upper()}")
            else:
                st.warning("No matching skills found.")

        with res_col2:
            st.subheader("❌ Missing Skills to Learn")
            if missing:
                for item in missing:
                    st.error(f"• {item.upper()}")
            else:
                st.info("No skills missing! Perfect candidate match.")

        # Matplotlib Chart Integration
        st.markdown("---")
        st.subheader("📈 Visual Breakdown")
        
        fig, ax = plt.subplots(figsize=(6, 3))
        bars = ax.bar(["Matched Skills", "Missing Skills"], [len(matched), len(missing)], color=['#2ecc71', '#e74c3c'], width=0.4)
        ax.set_ylabel("Count")
        ax.set_ylim(0, max(len(matched), len(missing), 1) + 2)
        
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval), ha='center', va='bottom')
            
        st.pyplot(fig)