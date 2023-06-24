from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Kiran Kumar Shah"
PAGE_ICON = ":wave:"
NAME = "Kiran Kumar Shah"
DESCRIPTION = """
FCCA|M.A(Eco)|DipIFRS|CAMS|CAMS-AUDIT|CFE|CISA|CISSP
"""
EMAIL = "kiran[.]shah[.]acca[@]email[.]com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/@KiranKumarShah",
    "LinkedIn": "https://www.linkedin.com/in/kirankumarshah/",
    "GitHub": "https://github.com/RiskSimplifier",
   "Instagram": "https://www.instagram.com/urban_sketcher_nepal?r=nametag"
}
# PROJECTS = {
#     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#     "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#     "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#     "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
# }


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=280)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # st.download_button(
    #     label=" 📄 Download Resume",
    #     data=PDFbyte,
    #     file_name=resume_file.name,
    #     mime="application/octet-stream",
    # )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Bio")
st.write(
    """
    Mr. Kiran Kumar Shah is a Risk Management Professional with knowledge and experience in different
    risk management areas including IT Audit, AML/CFT, Compliance, and Cyber Security. In his 12 years 
    of experience in various commercial banks, he was responsible for establishing Risk management 
    governance, IT Audit, creating policies and procedures, providing training, conducting financial 
    investigations, and so on.
    Under his leadership, Kumari Bank became one of the first five banks out of 28 commercial banks of
    Nepal to go live for goAML before the deadline given by regulatory bodies.

    He is also Nepal's first person with advanced ACAMS certification (CAMS-Audit).

    Mr.Kiran Kumar Shah and Siorik Consultancy teamed up to create this course AML/CFT Zero to Hero Couse
    to help beginners as well as professionals to help them master different aspects of AML/CFT. In this course
    you will be taught in theoretical aspects and how to apply that knowledge practically. You will
    be also introduced to tools like Power BI, Tableau, SQL, and Machine Learning to make you an efficient and 
    effective AML Analyst. So check out this course by visiting the following link.


# """
)
st.write('https://www.udemy.com/course/amlcft-zero-to-hero-course/?referralCode=CD51C836B3518E24CA71 👨‍🏫') 

# # --- SKILLS ---
# st.write('\n')
# st.subheader("Hard Skills")
# st.write(
#     """
# - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
# - 📊 Data Visulization: PowerBi, MS Excel, Plotly
# - 📚 Modeling: Logistic regression, linear regression, decition trees
# - 🗄️ Databases: Postgres, MongoDB, MySQL
# """
# )


# # --- WORK HISTORY ---
# st.write('\n')
# st.subheader("Work History")
# st.write("---")

# # --- JOB 1
# st.write("🚧", "**Senior Data Analyst | Ross Industries**")
# st.write("02/2020 - Present")
# st.write(
#     """
# - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
# - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
# - ► Redesigned data model through iterations that improved predictions by 12%
# """
# )

# # --- JOB 2
# st.write('\n')
# st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
# st.write("01/2018 - 02/2022")
# st.write(
#     """
# - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
# - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
# - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
# """
# )

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# # --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
