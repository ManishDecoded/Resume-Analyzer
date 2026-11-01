# 📄 Resume & Job Skill Matcher

An interactive Python web application that analyzes a candidate's resume against a job description to identify matching skills, highlight skill gaps, and calculate a compatibility score.

Built using **Streamlit, Regular Expressions (Regex), Python Set Operations, and Matplotlib**, this project demonstrates how text processing can simplify initial resume screening.

## ✨ Features

- 📊 **Match Score:** Calculates the percentage of required job skills found in the resume.
- ✅ **Matched Skills:** Identifies skills present in both the resume and job description.
- ❌ **Missing Skills:** Highlights required skills that are not detected in the resume.
- 📈 **Visual Analytics:** Displays a bar chart comparing matched and missing skills.
- 📝 **Interactive Interface:** Enter or edit resume and job description text directly in the application.
- 🔍 **Regex-Based Extraction:** Detects predefined skills using pattern matching and word boundaries.

## 🛠️ Technologies Used

- **Python** — Core programming logic
- **Streamlit** — Interactive web interface
- **Regular Expressions (Regex)** — Skill extraction from text
- **Set Operations** — Skill comparison and matching
- **Matplotlib** — Data visualization

## ⚙️ How It Works

1. Enter the candidate's resume and the target job description.
2. The application extracts recognized skills from both texts.
3. Python set operations identify matching and missing skills.
4. A match percentage is calculated based on the skills required by the job description.
5. Results are displayed through metrics, skill lists, a progress bar, and a bar chart.

**Match Score Formula:**

`Match Score = (Number of Matched Skills / Number of Required Skills) × 100`

## 🚀 Getting Started

### Prerequisites

Install Python 3.9 or later and ensure that `pip` is available.

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/Resume-Skill-Matcher.git
```

**2. Navigate to the project folder**

```bash
cd Resume-Skill-Matcher
```

**3. Install the required libraries**

```bash
pip install streamlit matplotlib
```

**4. Run the application**

Replace `app.py` with your Python filename if it is different.

```bash
streamlit run app.py
```

The application will open in your default browser.

## 📂 Project Structure

```text
Resume-Skill-Matcher/
│
├── app.py          # Main application
├── README.md       # Project documentation
└── .gitignore      # Git ignore rules
```

## 🎯 Project Objective

This project demonstrates the practical application of **text processing, algorithmic logic, set theory, and data visualization** in resume analysis and skill-gap identification.

It can help candidates understand which required skills are detected in their resumes and which skills may need further development.

## ⚠️ Limitations

- Uses a predefined skill database rather than a trained AI/ML model.
- Detects only the skills included in its predefined skill bank.
- The match score measures skill overlap, not a candidate's overall suitability for a role.

## 👨‍💻 Author

**Manish Kumar Singh**

MCA (AI & ML) Student | Chandigarh University

---

⭐ If you find this project useful, consider giving the repository a star!