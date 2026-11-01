# 📄 Resume & Job Skill Matcher

An interactive Python web application that analyzes a candidate's resume against a job description to identify matching skills, highlight skill gaps, and calculate a compatibility score.

Built using **Python, Streamlit, Regex, Set Operations, and Matplotlib**, this project demonstrates how text processing can simplify initial resume screening.

## ✨ Features

- 📊 **Match Score:** Calculates the percentage of required job skills found in the resume.
- ✅ **Matched Skills:** Identifies skills present in both the resume and job description.
- ❌ **Missing Skills:** Highlights required skills not detected in the resume.
- 📈 **Visual Analytics:** Displays a bar chart comparing matched and missing skills.
- 📝 **Interactive Interface:** Enter or edit resume and job description text directly in the application.
- 🔍 **Regex-Based Extraction:** Detects predefined skills using pattern matching and word boundaries.

## 🛠️ Technologies Used

- **Python** — Core programming logic
- **Streamlit** — Interactive web interface
- **Regular Expressions (Regex)** — Skill extraction
- **Set Operations** — Skill comparison and matching
- **Matplotlib** — Data visualization

## ⚙️ How It Works

1. Enter the candidate's resume and the target job description.
2. The application extracts recognized skills from both texts.
3. Set operations identify matching and missing skills.
4. The application calculates a match percentage based on the required job skills.
5. Results appear through metrics, skill lists, a progress bar, and a bar chart.

**Match Score Formula:**

`Match Score = (Number of Matched Skills / Number of Required Skills) × 100`

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or later
- Git

### Installation

**1. Clone the repository**

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/Resume-Skill-Matcher.git
```

**2. Navigate to the project directory**

```bash
cd Resume-Skill-Matcher
```

**3. Install the dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
streamlit run app.py
```

Replace `app.py` with your actual Python filename if it is different.

The application will open in your default browser.

## 📂 Project Structure

```text
Resume-Skill-Matcher/
│
├── app.py              # Main Python application
├── requirements.txt    # Required Python libraries
├── README.md           # Project documentation
└── .gitignore          # Excludes unnecessary and sensitive files
```

## 🎯 Project Objective

The objective is to demonstrate the practical application of **text processing, regular expressions, Python set operations, and data visualization** in resume analysis and skill-gap identification.

The application can help candidates identify which required skills are detected in their resumes and which skills may need further development.

## ⚠️ Limitations

- Uses a predefined skill database rather than a trained AI/ML model.
- Detects only skills included in its predefined skill bank.
- The match score measures skill overlap, not overall candidate suitability.
- Does not understand context or evaluate a candidate's actual proficiency.

## 👨‍💻 Author

**Manish Kumar Singh**  
MCA (AI & ML) Student | Chandigarh University

---

⭐ If you find this project useful, consider giving the repository a star!